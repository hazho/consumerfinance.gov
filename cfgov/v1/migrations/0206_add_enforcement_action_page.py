# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-02 18:22

import django.core.validators
import django.db.models.deletion
import modelcluster.fields
import v1.atomic_elements.organisms
import v1.blocks
from django.db import migrations, models
from wagtail.core import blocks as core_blocks
from wagtail.core import fields as core_fields
from wagtail.images import blocks as images_blocks


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0205_bureau_structure_multiple_leads'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnforcementActionPage',
            fields=[
                ('abstractfilterpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='v1.AbstractFilterPage')),
                ('sidebar_header', models.CharField(default='Action details', max_length=100)),
                ('court', models.CharField(blank=True, default='', max_length=150)),
                ('institution_type', models.CharField(choices=[('Nonbank', 'Nonbank'), ('Bank', 'Bank')], max_length=50)),
                ('docket_number', models.CharField(max_length=100)),
                ('content', core_fields.StreamField((('full_width_text', core_blocks.StreamBlock((('content', core_blocks.RichTextBlock(icon='edit')), ('content_with_anchor', core_blocks.StructBlock((('content_block', core_blocks.RichTextBlock()), ('anchor_link', core_blocks.StructBlock((('link_id', core_blocks.CharBlock(help_text='\n            ID will be auto-generated on save.\n            However, you may enter some human-friendly text that\n            will be incorporated to make it easier to read.\n        ', label='ID for this content block', required=False)),)))))), ('heading', core_blocks.StructBlock((('text', v1.blocks.HeadingTextBlock(required=False)), ('level', core_blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#the-icons">See full list of icons</a>', required=False))), required=False)), ('image', core_blocks.StructBlock((('image', core_blocks.StructBlock((('upload', images_blocks.ImageChooserBlock(required=False)), ('alt', core_blocks.CharBlock(help_text="If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))))), ('image_width', core_blocks.ChoiceBlock(choices=[('full', 'full'), (470, '470px'), (270, '270px'), (170, '170px')])), ('image_position', core_blocks.ChoiceBlock(choices=[('right', 'right'), ('left', 'left')], help_text='Does not apply if the image is full-width')), ('text', core_blocks.RichTextBlock(label='Caption', required=False)), ('is_bottom_rule', core_blocks.BooleanBlock(default=True, help_text='Check to add a horizontal rule line to bottom of inset.', label='Has bottom rule line', required=False))))), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('quote', core_blocks.StructBlock((('body', core_blocks.TextBlock()), ('citation', core_blocks.TextBlock(required=False)), ('is_large', core_blocks.BooleanBlock(required=False))))), ('cta', core_blocks.StructBlock((('slug_text', core_blocks.CharBlock(required=False)), ('paragraph_text', core_blocks.RichTextBlock(required=False)), ('button', core_blocks.StructBlock((('text', core_blocks.CharBlock(required=False)), ('url', core_blocks.CharBlock(default='/', required=False)), ('size', core_blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('large', 'Large Primary')])))))))), ('related_links', core_blocks.StructBlock((('heading', core_blocks.CharBlock(required=False)), ('paragraph', core_blocks.RichTextBlock(required=False)), ('links', core_blocks.ListBlock(core_blocks.StructBlock((('text', core_blocks.CharBlock(required=False)), ('url', core_blocks.CharBlock(default='/', required=False))))))))), ('reusable_text', v1.blocks.ReusableTextChooserBlock('v1.ReusableText')), ('email_signup', core_blocks.StructBlock((('heading', core_blocks.CharBlock(default='Stay informed', required=False)), ('default_heading', core_blocks.BooleanBlock(default=True, help_text='If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', label='Default heading style', required=False)), ('text', core_blocks.CharBlock(help_text='Write a sentence or two about what kinds of emails the user is signing up for, how frequently they will be sent, etc.', required=False)), ('gd_code', core_blocks.CharBlock(help_text='Code for the topic (i.e., mailing list) you want people who submit this form to subscribe to. Format: USCFPB_###', label='GovDelivery code', required=False)), ('disclaimer_page', core_blocks.PageChooserBlock(help_text='Choose the page that the "See Privacy Act statement" link should go to. If in doubt, use "Generic Email Sign-Up Privacy Act Statement".', label='Privacy Act statement', required=False))))), ('well', core_blocks.StructBlock((('content', core_blocks.RichTextBlock(label='Well', required=False)),))), ('well_with_ask_search', core_blocks.StructBlock((('content', core_blocks.RichTextBlock(label='Well', required=False)), ('ask_search', core_blocks.StructBlock((('show_label', core_blocks.BooleanBlock(default=True, help_text='Whether to show form label.', required=False)), ('placeholder', core_blocks.TextBlock(help_text='Text to show for the input placeholder text.', required=False))))))))))), ('expandable', core_blocks.StructBlock((('label', core_blocks.CharBlock(required=False)), ('is_bordered', core_blocks.BooleanBlock(required=False)), ('is_midtone', core_blocks.BooleanBlock(required=False)), ('is_expanded', core_blocks.BooleanBlock(required=False)), ('content', core_blocks.StreamBlock((('paragraph', core_blocks.RichTextBlock(required=False)), ('well', core_blocks.StructBlock((('content', core_blocks.RichTextBlock(label='Well', required=False)),))), ('links', core_blocks.StructBlock((('text', core_blocks.CharBlock(required=False)), ('url', core_blocks.CharBlock(default='/', required=False))))), ('email', core_blocks.StructBlock((('emails', core_blocks.ListBlock(core_blocks.StructBlock((('url', core_blocks.EmailBlock(label='Email address')), ('text', core_blocks.CharBlock(label='Link text (optional)', required=False)))))),))), ('phone', core_blocks.StructBlock((('fax', core_blocks.BooleanBlock(default=False, label='Is this number a fax?', required=False)), ('phones', core_blocks.ListBlock(core_blocks.StructBlock((('number', core_blocks.CharBlock(help_text='Do not include spaces or dashes. Ex. 8554112372', max_length=15, validators=[django.core.validators.RegexValidator(message='Enter a numeric phone number, without punctuation.', regex='^\\d*$')])), ('extension', core_blocks.CharBlock(max_length=4, required=False)), ('vanity', core_blocks.CharBlock(help_text='A phoneword version of the above number. Include any formatting. Ex. (555) 222-CFPB', max_length=15, required=False)), ('tty', core_blocks.CharBlock(help_text='Do not include spaces or dashes. Ex. 8554112372', label='TTY', max_length=15, required=False, validators=[django.core.validators.RegexValidator(message='Enter a numeric phone number, without punctuation.', regex='^\\d*$')])), ('tty_ext', core_blocks.CharBlock(label='TTY Extension', max_length=4, required=False))))))))), ('address', core_blocks.StructBlock((('label', core_blocks.CharBlock(required=False)), ('title', core_blocks.CharBlock(required=False)), ('street', core_blocks.CharBlock(required=False)), ('city', core_blocks.CharBlock(max_length=50, required=False)), ('state', core_blocks.CharBlock(max_length=25, required=False)), ('zip_code', core_blocks.CharBlock(max_length=15, required=False)))))), blank=True))))), ('expandable_group', core_blocks.StructBlock((('heading', core_blocks.CharBlock(help_text='Added as an <code>&lt;h3&gt;</code> at the top of this block. Also adds a wrapping <code>&lt;div&gt;</code> whose <code>id</code> attribute comes from a slugified version of this heading, creating an anchor that can be used when linking to this part of the page.', required=False)), ('body', core_blocks.RichTextBlock(required=False)), ('is_accordion', core_blocks.BooleanBlock(required=False)), ('has_top_rule_line', core_blocks.BooleanBlock(default=False, help_text='Check this to add a horizontal rule line to top of expandable group.', required=False)), ('expandables', core_blocks.ListBlock(core_blocks.StructBlock((('label', core_blocks.CharBlock(required=False)), ('is_bordered', core_blocks.BooleanBlock(required=False)), ('is_midtone', core_blocks.BooleanBlock(required=False)), ('is_expanded', core_blocks.BooleanBlock(required=False)), ('content', core_blocks.StreamBlock((('paragraph', core_blocks.RichTextBlock(required=False)), ('well', core_blocks.StructBlock((('content', core_blocks.RichTextBlock(label='Well', required=False)),))), ('links', core_blocks.StructBlock((('text', core_blocks.CharBlock(required=False)), ('url', core_blocks.CharBlock(default='/', required=False))))), ('email', core_blocks.StructBlock((('emails', core_blocks.ListBlock(core_blocks.StructBlock((('url', core_blocks.EmailBlock(label='Email address')), ('text', core_blocks.CharBlock(label='Link text (optional)', required=False)))))),))), ('phone', core_blocks.StructBlock((('fax', core_blocks.BooleanBlock(default=False, label='Is this number a fax?', required=False)), ('phones', core_blocks.ListBlock(core_blocks.StructBlock((('number', core_blocks.CharBlock(help_text='Do not include spaces or dashes. Ex. 8554112372', max_length=15, validators=[django.core.validators.RegexValidator(message='Enter a numeric phone number, without punctuation.', regex='^\\d*$')])), ('extension', core_blocks.CharBlock(max_length=4, required=False)), ('vanity', core_blocks.CharBlock(help_text='A phoneword version of the above number. Include any formatting. Ex. (555) 222-CFPB', max_length=15, required=False)), ('tty', core_blocks.CharBlock(help_text='Do not include spaces or dashes. Ex. 8554112372', label='TTY', max_length=15, required=False, validators=[django.core.validators.RegexValidator(message='Enter a numeric phone number, without punctuation.', regex='^\\d*$')])), ('tty_ext', core_blocks.CharBlock(label='TTY Extension', max_length=4, required=False))))))))), ('address', core_blocks.StructBlock((('label', core_blocks.CharBlock(required=False)), ('title', core_blocks.CharBlock(required=False)), ('street', core_blocks.CharBlock(required=False)), ('city', core_blocks.CharBlock(max_length=50, required=False)), ('state', core_blocks.CharBlock(max_length=25, required=False)), ('zip_code', core_blocks.CharBlock(max_length=15, required=False)))))), blank=True))))))))), ('notification', core_blocks.StructBlock((('message', core_blocks.CharBlock(help_text='The main notification message to display.', required=True)), ('explanation', core_blocks.TextBlock(help_text='Explanation text appears below the message in smaller type.', required=False)), ('links', core_blocks.ListBlock(core_blocks.StructBlock((('text', core_blocks.CharBlock(required=False)), ('url', core_blocks.CharBlock(default='/', required=False)))), help_text='Links appear on their own lines below the explanation.', required=False))))), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('feedback', core_blocks.StructBlock((('was_it_helpful_text', core_blocks.CharBlock(default='Was this page helpful to you?', help_text='Use this field only for feedback forms that use "Was this helpful?" radio buttons.', required=False)), ('intro_text', core_blocks.CharBlock(help_text='Optional feedback intro', required=False)), ('question_text', core_blocks.CharBlock(help_text='Optional expansion on intro', required=False)), ('radio_intro', core_blocks.CharBlock(help_text='Leave blank unless you are building a feedback form with extra radio-button prompts, as in /owning-a-home/help-us-improve/.', required=False)), ('radio_text', core_blocks.CharBlock(default='This information helps us understand your question better.', required=False)), ('radio_question_1', core_blocks.CharBlock(default='How soon do you expect to buy a home?', required=False)), ('radio_question_2', core_blocks.CharBlock(default='Do you currently own a home?', required=False)), ('button_text', core_blocks.CharBlock(default='Submit')), ('contact_advisory', core_blocks.RichTextBlock(help_text='Use only for feedback forms that ask for a contact email', required=False)))))), blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('v1.abstractfilterpage',),
        ),
        migrations.CreateModel(
            name='EnforcementActionStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(blank=True, max_length=200)),
                ('status', models.CharField(choices=[('Post Order/Post Judgment', 'Post Order/Post Judgment'), ('Expired/Terminated/Dismissed', 'Expired/Terminated/Dismissed'), ('Pending Litigation', 'Pending Litigation')], max_length=50)),
                ('action', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to='v1.EnforcementActionPage')),
            ],
        ),
    ]
