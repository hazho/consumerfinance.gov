# Generated by Django 2.2.16 on 2021-03-18 19:34

import v1.atomic_elements.organisms
import v1.blocks
import v1.util.ref
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0251_update_notification_default_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browsefilterablepage',
            name='content',
            field=wagtail.core.fields.StreamField([('full_width_text', wagtail.core.blocks.StreamBlock([('content', wagtail.core.blocks.RichTextBlock(icon='edit')), ('content_with_anchor', wagtail.core.blocks.StructBlock([('content_block', wagtail.core.blocks.RichTextBlock()), ('anchor_link', wagtail.core.blocks.StructBlock([('link_id', wagtail.core.blocks.CharBlock(help_text='\n            ID will be auto-generated on save.\n            However, you may enter some human-friendly text that\n            will be incorporated to make it easier to read.\n        ', label='ID for this content block', required=False))]))])), ('heading', wagtail.core.blocks.StructBlock([('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.core.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.core.blocks.StructBlock([('upload', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.core.blocks.CharBlock(help_text="If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), ('image_width', wagtail.core.blocks.ChoiceBlock(choices=[('full', 'full'), (470, '470px'), (270, '270px'), (170, '170px')])), ('image_position', wagtail.core.blocks.ChoiceBlock(choices=[('right', 'right'), ('left', 'left')], help_text='Does not apply if the image is full-width')), ('text', wagtail.core.blocks.RichTextBlock(label='Caption', required=False)), ('is_bottom_rule', wagtail.core.blocks.BooleanBlock(default=True, help_text='Check to add a horizontal rule line to bottom of inset.', label='Has bottom rule line', required=False))])), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('quote', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.TextBlock()), ('citation', wagtail.core.blocks.TextBlock(required=False)), ('is_large', wagtail.core.blocks.BooleanBlock(required=False))])), ('cta', wagtail.core.blocks.StructBlock([('slug_text', wagtail.core.blocks.CharBlock(required=False)), ('paragraph_text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('large', 'Large Primary')]))]))])), ('related_links', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False))])))])), ('reusable_text', v1.blocks.ReusableTextChooserBlock('v1.ReusableText')), ('email_signup', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Stay informed', required=False)), ('default_heading', wagtail.core.blocks.BooleanBlock(default=True, help_text='If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', label='Default heading style', required=False)), ('text', wagtail.core.blocks.CharBlock(help_text='Write a sentence or two about what kinds of emails the user is signing up for, how frequently they will be sent, etc.', required=False)), ('gd_code', wagtail.core.blocks.CharBlock(help_text='Code for the topic (i.e., mailing list) you want people who submit this form to subscribe to. Format: USCFPB_###', label='GovDelivery code', required=False)), ('disclaimer_page', wagtail.core.blocks.PageChooserBlock(help_text='Choose the page that the "See Privacy Act statement" link should go to. If in doubt, use "Generic Email Sign-Up Privacy Act Statement".', label='Privacy Act statement', required=False))])), ('well', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(label='Well', required=False))])), ('well_with_ask_search', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(label='Well', required=False)), ('ask_search', wagtail.core.blocks.StructBlock([('show_label', wagtail.core.blocks.BooleanBlock(default=True, help_text='Whether to show form label.', required=False)), ('placeholder', wagtail.core.blocks.TextBlock(help_text='Text to show for the input placeholder text.', required=False))]))]))])), ('filter_controls', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('is_bordered', wagtail.core.blocks.BooleanBlock(required=False)), ('is_midtone', wagtail.core.blocks.BooleanBlock(required=False)), ('is_expanded', wagtail.core.blocks.BooleanBlock(required=False)), ('title', wagtail.core.blocks.BooleanBlock(default=True, label='Filter Title', required=False)), ('no_posts_message', wagtail.core.blocks.CharBlock(help_text='Message for the <a href="https://cfpb.github.io/design-system/components/notifications#default-base-notification">notification</a> that will be displayed instead of filter controls if there are no posts to filter.', required=False)), ('no_posts_explanation', wagtail.core.blocks.CharBlock(help_text='Additional explanation for the notification that will be displayed if there are no posts to filter.', required=False)), ('post_date_description', wagtail.core.blocks.CharBlock(help_text='Strongly encouraged to help users understand the action that the date of the post is linked to, i.e. published, issued, released.', label='Date stamp descriptor', required=False)), ('categories', wagtail.core.blocks.StructBlock([('filter_category', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('show_preview_categories', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('page_type', wagtail.core.blocks.ChoiceBlock(choices=v1.util.ref.filterable_list_page_types, required=False))])), ('topic_filtering', wagtail.core.blocks.ChoiceBlock(choices=[('no_filter', "Don't filter topics"), ('sort_alphabetically', 'Filter topics, sort topic list alphabetically'), ('sort_by_frequency', 'Filter topics, sort topic list by number of results')], help_text='Whether to include a dropdown in the filter controls for "Topics"')), ('order_by', wagtail.core.blocks.ChoiceBlock(choices=[('-date_published', 'Date Published'), ('_score', 'Relevance')], help_text='How to order results')), ('statuses', wagtail.core.blocks.BooleanBlock(default=False, label='Filter Enforcement Statuses', required=False)), ('products', wagtail.core.blocks.BooleanBlock(default=False, label='Filter Enforcement Products', required=False)), ('authors', wagtail.core.blocks.BooleanBlock(default=True, label='Filter Authors', required=False)), ('date_range', wagtail.core.blocks.BooleanBlock(default=True, label='Filter Date Range', required=False)), ('output_5050', wagtail.core.blocks.BooleanBlock(default=False, label='Render preview items as 50-50s', required=False)), ('link_image_and_heading', wagtail.core.blocks.BooleanBlock(default=False, help_text='Add links to post preview images and headings in filterable list results', required=False)), ('filter_children', wagtail.core.blocks.BooleanBlock(default=True, help_text='If checked this list will only filter its child pages. If both children and siblings are checked, only child pages will be filtered.', required=False)), ('filter_siblings', wagtail.core.blocks.BooleanBlock(default=False, help_text='If checked this list will only filter its sibling pages. If both children and siblings are checked, only child pages will be filtered.', required=False))])), ('feedback', wagtail.core.blocks.StructBlock([('was_it_helpful_text', wagtail.core.blocks.CharBlock(default='Was this page helpful to you?', help_text='Use this field only for feedback forms that use "Was this helpful?" radio buttons.', required=False)), ('intro_text', wagtail.core.blocks.CharBlock(help_text='Optional feedback intro', required=False)), ('question_text', wagtail.core.blocks.CharBlock(help_text='Optional expansion on intro', required=False)), ('radio_intro', wagtail.core.blocks.CharBlock(help_text='Leave blank unless you are building a feedback form with extra radio-button prompts, as in /owning-a-home/help-us-improve/.', required=False)), ('radio_text', wagtail.core.blocks.CharBlock(default='This information helps us understand your question better.', required=False)), ('radio_question_1', wagtail.core.blocks.CharBlock(default='How soon do you expect to buy a home?', required=False)), ('radio_question_2', wagtail.core.blocks.CharBlock(default='Do you currently own a home?', required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Submit')), ('contact_advisory', wagtail.core.blocks.RichTextBlock(help_text='Use only for feedback forms that ask for a contact email', required=False))]))]),
        ),
        migrations.AlterField(
            model_name='sublandingfilterablepage',
            name='content',
            field=wagtail.core.fields.StreamField([('text_introduction', wagtail.core.blocks.StructBlock([('eyebrow', wagtail.core.blocks.CharBlock(help_text='Optional: Adds an H5 eyebrow above H1 heading text. Only use in conjunction with heading.', label='Pre-heading', required=False)), ('heading', wagtail.core.blocks.CharBlock(required=False)), ('intro', wagtail.core.blocks.RichTextBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock(required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False))]), required=False)), ('has_rule', wagtail.core.blocks.BooleanBlock(help_text='Check this to add a horizontal rule line to bottom of text introduction.', label='Has bottom rule', required=False))])), ('full_width_text', wagtail.core.blocks.StreamBlock([('content', wagtail.core.blocks.RichTextBlock(icon='edit')), ('content_with_anchor', wagtail.core.blocks.StructBlock([('content_block', wagtail.core.blocks.RichTextBlock()), ('anchor_link', wagtail.core.blocks.StructBlock([('link_id', wagtail.core.blocks.CharBlock(help_text='\n            ID will be auto-generated on save.\n            However, you may enter some human-friendly text that\n            will be incorporated to make it easier to read.\n        ', label='ID for this content block', required=False))]))])), ('heading', wagtail.core.blocks.StructBlock([('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.core.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.core.blocks.StructBlock([('upload', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.core.blocks.CharBlock(help_text="If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), ('image_width', wagtail.core.blocks.ChoiceBlock(choices=[('full', 'full'), (470, '470px'), (270, '270px'), (170, '170px')])), ('image_position', wagtail.core.blocks.ChoiceBlock(choices=[('right', 'right'), ('left', 'left')], help_text='Does not apply if the image is full-width')), ('text', wagtail.core.blocks.RichTextBlock(label='Caption', required=False)), ('is_bottom_rule', wagtail.core.blocks.BooleanBlock(default=True, help_text='Check to add a horizontal rule line to bottom of inset.', label='Has bottom rule line', required=False))])), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('quote', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.TextBlock()), ('citation', wagtail.core.blocks.TextBlock(required=False)), ('is_large', wagtail.core.blocks.BooleanBlock(required=False))])), ('cta', wagtail.core.blocks.StructBlock([('slug_text', wagtail.core.blocks.CharBlock(required=False)), ('paragraph_text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('large', 'Large Primary')]))]))])), ('related_links', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False))])))])), ('reusable_text', v1.blocks.ReusableTextChooserBlock('v1.ReusableText')), ('email_signup', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Stay informed', required=False)), ('default_heading', wagtail.core.blocks.BooleanBlock(default=True, help_text='If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', label='Default heading style', required=False)), ('text', wagtail.core.blocks.CharBlock(help_text='Write a sentence or two about what kinds of emails the user is signing up for, how frequently they will be sent, etc.', required=False)), ('gd_code', wagtail.core.blocks.CharBlock(help_text='Code for the topic (i.e., mailing list) you want people who submit this form to subscribe to. Format: USCFPB_###', label='GovDelivery code', required=False)), ('disclaimer_page', wagtail.core.blocks.PageChooserBlock(help_text='Choose the page that the "See Privacy Act statement" link should go to. If in doubt, use "Generic Email Sign-Up Privacy Act Statement".', label='Privacy Act statement', required=False))])), ('well', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(label='Well', required=False))])), ('well_with_ask_search', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(label='Well', required=False)), ('ask_search', wagtail.core.blocks.StructBlock([('show_label', wagtail.core.blocks.BooleanBlock(default=True, help_text='Whether to show form label.', required=False)), ('placeholder', wagtail.core.blocks.TextBlock(help_text='Text to show for the input placeholder text.', required=False))]))]))])), ('filter_controls', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('is_bordered', wagtail.core.blocks.BooleanBlock(required=False)), ('is_midtone', wagtail.core.blocks.BooleanBlock(required=False)), ('is_expanded', wagtail.core.blocks.BooleanBlock(required=False)), ('title', wagtail.core.blocks.BooleanBlock(default=True, label='Filter Title', required=False)), ('no_posts_message', wagtail.core.blocks.CharBlock(help_text='Message for the <a href="https://cfpb.github.io/design-system/components/notifications#default-base-notification">notification</a> that will be displayed instead of filter controls if there are no posts to filter.', required=False)), ('no_posts_explanation', wagtail.core.blocks.CharBlock(help_text='Additional explanation for the notification that will be displayed if there are no posts to filter.', required=False)), ('post_date_description', wagtail.core.blocks.CharBlock(help_text='Strongly encouraged to help users understand the action that the date of the post is linked to, i.e. published, issued, released.', label='Date stamp descriptor', required=False)), ('categories', wagtail.core.blocks.StructBlock([('filter_category', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('show_preview_categories', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('page_type', wagtail.core.blocks.ChoiceBlock(choices=v1.util.ref.filterable_list_page_types, required=False))])), ('topic_filtering', wagtail.core.blocks.ChoiceBlock(choices=[('no_filter', "Don't filter topics"), ('sort_alphabetically', 'Filter topics, sort topic list alphabetically'), ('sort_by_frequency', 'Filter topics, sort topic list by number of results')], help_text='Whether to include a dropdown in the filter controls for "Topics"')), ('order_by', wagtail.core.blocks.ChoiceBlock(choices=[('-date_published', 'Date Published'), ('_score', 'Relevance')], help_text='How to order results')), ('statuses', wagtail.core.blocks.BooleanBlock(default=False, label='Filter Enforcement Statuses', required=False)), ('products', wagtail.core.blocks.BooleanBlock(default=False, label='Filter Enforcement Products', required=False)), ('authors', wagtail.core.blocks.BooleanBlock(default=True, label='Filter Authors', required=False)), ('date_range', wagtail.core.blocks.BooleanBlock(default=True, label='Filter Date Range', required=False)), ('output_5050', wagtail.core.blocks.BooleanBlock(default=False, label='Render preview items as 50-50s', required=False)), ('link_image_and_heading', wagtail.core.blocks.BooleanBlock(default=False, help_text='Add links to post preview images and headings in filterable list results', required=False)), ('filter_children', wagtail.core.blocks.BooleanBlock(default=True, help_text='If checked this list will only filter its child pages. If both children and siblings are checked, only child pages will be filtered.', required=False)), ('filter_siblings', wagtail.core.blocks.BooleanBlock(default=False, help_text='If checked this list will only filter its sibling pages. If both children and siblings are checked, only child pages will be filtered.', required=False))])), ('featured_content', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.TextBlock(help_text='Line breaks will be ignored.')), ('post', wagtail.core.blocks.PageChooserBlock(required=False)), ('show_post_link', wagtail.core.blocks.BooleanBlock(label='Render post link?', required=False)), ('post_link_text', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.core.blocks.StructBlock([('upload', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.core.blocks.CharBlock(help_text="If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False))]), label='Additional Links')), ('video', wagtail.core.blocks.StructBlock([('video_id', wagtail.core.blocks.RegexBlock(error_messages={'invalid': 'The YouTube video ID is in the wrong format.'}, help_text='Enter the YouTube video ID, which is located at the end of the video URL, after "v=". For example, the video ID for https://www.youtube.com/watch?v=1V0Ax9OIc84 is 1V0Ax9OIc84.', label='YouTube video ID', regex='^[\\w-]{11}$', required=False)), ('thumbnail_image', wagtail.images.blocks.ImageChooserBlock(help_text='Optional thumbnail image to show before and after the video plays. If the thumbnail image is not set here, the video player will default to showing the thumbnail that was set in (or automatically chosen by) YouTube.', required=False))], required=False))])), ('feedback', wagtail.core.blocks.StructBlock([('was_it_helpful_text', wagtail.core.blocks.CharBlock(default='Was this page helpful to you?', help_text='Use this field only for feedback forms that use "Was this helpful?" radio buttons.', required=False)), ('intro_text', wagtail.core.blocks.CharBlock(help_text='Optional feedback intro', required=False)), ('question_text', wagtail.core.blocks.CharBlock(help_text='Optional expansion on intro', required=False)), ('radio_intro', wagtail.core.blocks.CharBlock(help_text='Leave blank unless you are building a feedback form with extra radio-button prompts, as in /owning-a-home/help-us-improve/.', required=False)), ('radio_text', wagtail.core.blocks.CharBlock(default='This information helps us understand your question better.', required=False)), ('radio_question_1', wagtail.core.blocks.CharBlock(default='How soon do you expect to buy a home?', required=False)), ('radio_question_2', wagtail.core.blocks.CharBlock(default='Do you currently own a home?', required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Submit')), ('contact_advisory', wagtail.core.blocks.RichTextBlock(help_text='Use only for feedback forms that ask for a contact email', required=False))]))]),
        ),
    ]
