import json
from datetime import datetime
from io import StringIO

from django.test import TestCase

from wagtail.core.models import Site

from dateutil.relativedelta import relativedelta
from mock import patch
from pytz import timezone

from search.elasticsearch_helpers import ElasticsearchTestsMixin
from v1.documents import (
    EnforcementActionFilterablePagesDocumentSearch,
    EventFilterablePagesDocumentSearch,
    FilterablePagesDocument,
    FilterablePagesDocumentSearch,
)
from v1.models.base import CFGOVPageCategory
from v1.models.blog_page import BlogPage
from v1.models.enforcement_action_page import (
    EnforcementActionPage,
    EnforcementActionProduct,
    EnforcementActionStatus,
)
from v1.models.learn_page import AbstractFilterPage, EventPage
from v1.tests.wagtail_pages.helpers import publish_page


class FilterablePagesDocumentTest(TestCase):
    def test_model_class_added(self):
        self.assertEqual(
            FilterablePagesDocument.django.model, AbstractFilterPage
        )

    def test_ignore_signal_default(self):
        self.assertFalse(FilterablePagesDocument.django.ignore_signals)

    def test_auto_refresh_default(self):
        self.assertFalse(FilterablePagesDocument.django.auto_refresh)

    def test_fields_populated(self):
        mapping = FilterablePagesDocument._doc_type.mapping
        self.assertCountEqual(
            mapping.properties.properties.to_dict().keys(),
            [
                "tags",
                "categories",
                "language",
                "title",
                "url",
                "is_archived",
                "date_published",
                "start_dt",
                "end_dt",
                "statuses",
                "products",
                "initial_filing_date",
                "model_class",
                "content",
                "preview_description",
                "path",
                "depth",
            ],
        )

    def test_get_queryset(self):
        test_event = EventPage(
            title="Testing", start_dt=datetime.now(timezone("UTC"))
        )
        qs = FilterablePagesDocument().get_queryset()
        self.assertFalse(qs.filter(title=test_event.title).exists())

    def test_prepare_statuses(self):
        enforcement = EnforcementActionPage(
            title="Great Test Page",
            preview_description="This is a great test page.",
            initial_filing_date=datetime.now(timezone("UTC")),
        )
        status = EnforcementActionStatus(status="expired-terminated-dismissed")
        enforcement.statuses.add(status)
        doc = FilterablePagesDocument()
        prepared_data = doc.prepare(enforcement)
        self.assertEqual(
            prepared_data["statuses"], ["expired-terminated-dismissed"]
        )

    def test_prepare_content_no_content_defined(self):
        event = EventPage(
            title="Event Test", start_dt=datetime.now(timezone("UTC"))
        )
        doc = FilterablePagesDocument()
        prepared_data = doc.prepare(event)
        self.assertIsNone(prepared_data["content"])

    def test_prepare_content_exists(self):
        blog = BlogPage(
            title="Test Blog",
            content=json.dumps(
                [
                    {
                        "type": "full_width_text",
                        "value": [
                            {
                                "type": "content",
                                "value": "Blog Text",
                            },
                        ],
                    },
                ]
            ),
        )
        doc = FilterablePagesDocument()
        prepared_data = doc.prepare(blog)
        self.assertEqual(prepared_data["content"], "Blog Text")

    def test_prepare_content_empty(self):
        blog = BlogPage(title="Test Blog", content=json.dumps([]))
        doc = FilterablePagesDocument()
        prepared_data = doc.prepare(blog)
        self.assertIsNone(prepared_data["content"])

    def test_prepare_products(self):
        enforcement = EnforcementActionPage(
            title="Great Test Page",
            preview_description="This is a great test page.",
            initial_filing_date=datetime.now(timezone("UTC")),
        )
        product = EnforcementActionProduct(product="Fair Lending")
        enforcement.products.add(product)
        doc = FilterablePagesDocument()
        prepared_data = doc.prepare(enforcement)
        self.assertEqual(prepared_data["products"], ["Fair Lending"])


class FilterablePagesDocumentSearchTest(ElasticsearchTestsMixin, TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.site = Site.objects.get(is_default_site=True)

        content = json.dumps(
            [
                {
                    "type": "full_width_text",
                    "value": [
                        {
                            "type": "content",
                            "value": "Foo Test Content",
                        },
                    ],
                },
            ]
        )

        event = EventPage(
            title="Event Test",
            start_dt=datetime(2021, 2, 16, tzinfo=timezone("UTC")),
            end_dt=datetime(2021, 2, 16, tzinfo=timezone("UTC")),
        )
        event.tags.add("test-topic")
        event.categories.add(CFGOVPageCategory(name="test-category"))
        event.language = "es"
        publish_page(event)
        enforcement = EnforcementActionPage(
            title="Great Test Page",
            preview_description="This is a great test page.",
            initial_filing_date=datetime.now(timezone("UTC")),
        )
        status = EnforcementActionStatus(status="expired-terminated-dismissed")
        enforcement.statuses.add(status)
        product = EnforcementActionProduct(product="Debt Collection")
        enforcement.products.add(product)
        publish_page(enforcement)
        blog = BlogPage(title="Blog Page")
        publish_page(blog)

        blog_title_match = BlogPage(title="Foo Bar")
        publish_page(blog_title_match)

        blog_preview_match = BlogPage(
            title="Random Title", preview_description="Foo blog"
        )
        publish_page(blog_preview_match)

        blog_content_match = BlogPage(title="Some Title", content=content)
        publish_page(blog_content_match)

        blog_topic_match = BlogPage(title="Another Blog Post")
        blog_topic_match.tags.add("Foo Tag")
        publish_page(blog_topic_match)

        cls.event = event
        cls.enforcement = enforcement
        cls.blog = blog
        cls.blog_title_match = blog_title_match
        cls.blog_preview_match = blog_preview_match
        cls.blog_content_match = blog_content_match
        cls.blog_topic_match = blog_topic_match

        cls.rebuild_elasticsearch_index("v1", stdout=StringIO())

    def test_search_event_all_fields(self):
        to_date_dt = datetime(2021, 3, 16)
        to_date = datetime.date(to_date_dt)
        from_date_dt = datetime(2021, 1, 16)
        from_date = datetime.date(from_date_dt)

        search = EventFilterablePagesDocumentSearch(prefix="/")
        search.filter(
            topics=["test-topic"],
            categories=["test-category"],
            language=["es"],
            to_date=to_date,
            from_date=from_date,
            archived=["no"],
        )
        results = search.search(title="Event Test")
        self.assertTrue(results.filter(title=self.event.title).exists())

    def test_search_blog_dates(self):
        to_date_dt = datetime.today() + relativedelta(months=1)
        to_date = datetime.date(to_date_dt)
        from_date_dt = datetime.today() - relativedelta(months=1)
        from_date = datetime.date(from_date_dt)

        search = FilterablePagesDocumentSearch(prefix="/")
        search.filter(
            topics=[],
            categories=[],
            language=[],
            to_date=to_date,
            from_date=from_date,
            archived=None,
        )
        results = search.search(title=None)
        self.assertTrue(results.filter(title=self.blog.title).exists())

    def test_search_enforcement_actions(self):
        to_date_dt = datetime.today() + relativedelta(months=1)
        to_date = datetime.date(to_date_dt)
        from_date_dt = datetime.today() - relativedelta(months=1)
        from_date = datetime.date(from_date_dt)

        search = EnforcementActionFilterablePagesDocumentSearch(prefix="/")
        search.filter(
            topics=[],
            categories=[],
            language=[],
            to_date=to_date,
            from_date=from_date,
            statuses=["expired-terminated-dismissed"],
            products=["Debt Collection"],
            archived=None,
        )
        results = search.search(title=None)
        self.assertTrue(results.filter(title=self.enforcement.title).exists())

    def test_search_enforcement_actions_no_statuses(self):
        to_date_dt = datetime.today() + relativedelta(months=1)
        to_date = datetime.date(to_date_dt)
        from_date_dt = datetime.today() - relativedelta(months=1)
        from_date = datetime.date(from_date_dt)

        search = EnforcementActionFilterablePagesDocumentSearch(prefix="/")
        search.filter(
            topics=[],
            categories=[],
            language=[],
            to_date=to_date,
            from_date=from_date,
            statuses=[],
            products=[],
            archived=None,
        )
        results = search.search(title=None)
        self.assertTrue(results.filter(title=self.enforcement.title).exists())

    def test_search_title_uses_multimatch(self):
        search = FilterablePagesDocumentSearch(prefix="/")
        search.filter(
            topics=[],
            categories=[],
            language=[],
            to_date=None,
            from_date=None,
            archived=None,
        )
        results = search.search(title="Foo")
        self.assertTrue(results.filter(title=self.blog_title_match).exists())
        self.assertTrue(
            results.filter(title=self.blog_content_match.title).exists()
        )
        self.assertTrue(
            results.filter(title=self.blog_preview_match.title).exists()
        )
        self.assertTrue(
            results.filter(title=self.blog_topic_match.title).exists()
        )


class TestThatWagtailPageSignalsUpdateIndex(ElasticsearchTestsMixin, TestCase):
    def test_index_reflects_page_moves_and_deletions(self):
        root = Site.objects.get(is_default_site=True).root_page

        parent = BlogPage(title="parent", live=True)
        root.add_child(instance=parent)

        blog1 = BlogPage(title="foo 1", live=True)
        parent.add_child(instance=blog1)

        blog2 = BlogPage(title="foo 2", live=True)
        parent.add_child(instance=blog2)

        blog3 = BlogPage(title="foo 3", live=True)
        parent.add_child(instance=blog3)

        self.rebuild_elasticsearch_index("v1", stdout=StringIO())
        search = FilterablePagesDocumentSearch(prefix="/parent/")

        # Initially a search at the root should return 3 results.
        results = search.search(title="foo")
        self.assertEqual(results.count(), 3)

        # By default we set ELASTICSEARCH_DSL_AUTOSYNC to False in
        # settings.test, and there's unfortunately no better way to override
        # that here than by patching; see
        # https://github.com/django-es/django-elasticsearch-dsl/issues/322.
        with patch(
            "django_elasticsearch_dsl.registries.DEDConfig.autosync_enabled",
            return_value=True,
        ):
            # Moving a page out of the parent should update the index so that
            # a search there now returns only 2 results.
            blog2.move(root)
            results = search.search(title="foo")
            self.assertEqual(results.count(), 2)

            # Updating a page should also update the index so that a search
            # now returns only 1 result.
            blog3.title = "bar"
            blog3.save_revision().publish()
            results = search.search(title="foo")
            self.assertEqual(results.count(), 1)

            # Deleting the remaining page with "blog" in the root should
            # result in an empty search result.
            blog1.delete()
            results = search.search(title="foo")
            self.assertEqual(results.count(), 0)
