# Generated by Django 3.2.12 on 2022-03-31 18:19

from django.db import migrations

import wagtail.core.blocks
import wagtail.core.fields
import wagtail.snippets.blocks

import v1.atomic_elements.molecules
import v1.blocks
import v1.models.snippets


class Migration(migrations.Migration):

    dependencies = [
        ('ask_cfpb', '0039_2022_squash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerpage',
            name='sidebar',
            field=wagtail.core.fields.StreamField([('call_to_action', wagtail.core.blocks.StructBlock([('slug_text', wagtail.core.blocks.CharBlock(required=False)), ('paragraph_text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('aria_label', wagtail.core.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('large', 'Large Primary')]))]))])), ('related_links', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('aria_label', wagtail.core.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False))])))])), ('related_metadata', wagtail.core.blocks.StructBlock([('slug', wagtail.core.blocks.CharBlock(max_length=100)), ('content', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100)), ('blob', wagtail.core.blocks.RichTextBlock())], icon='pilcrow')), ('list', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('aria_label', wagtail.core.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False))])))], icon='list-ul')), ('date', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100)), ('date', wagtail.core.blocks.DateBlock())], icon='date')), ('topics', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Topics', max_length=100)), ('show_topics', wagtail.core.blocks.BooleanBlock(default=True, required=False))], icon='tag'))])), ('is_half_width', wagtail.core.blocks.BooleanBlock(default=False, required=False))])), ('email_signup', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Stay informed', required=False)), ('default_heading', wagtail.core.blocks.BooleanBlock(default=True, help_text='If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', label='Default heading style', required=False)), ('text', wagtail.core.blocks.CharBlock(help_text='Write a sentence or two about what kinds of emails the user is signing up for, how frequently they will be sent, etc.', required=False)), ('signup_method', wagtail.core.blocks.ChoiceBlock(choices=[('form', 'Enter an email address directly in a form'), ('link', 'Link to a GovDelivery signup page')], help_text='Choose how people will sign up: either by entering their email directly or by going to a GovDelivery signup page', label='Signup method')), ('gd_code', wagtail.core.blocks.CharBlock(help_text='For a signup form, GovDeliery code (USCFPB_###) for the list people who submit the form will sign up for. For a signup link, URL for the GovDelivery signup page.', label='GovDelivery code or signup page URL', required=False)), ('disclaimer_page', wagtail.core.blocks.PageChooserBlock(help_text='Choose the page that the "See Privacy Act statement" link should go to. If in doubt, use "Generic Email Sign-Up Privacy Act Statement".', label='Privacy Act statement', required=False))])), ('sidebar_contact', wagtail.core.blocks.StructBlock([('contact', wagtail.snippets.blocks.SnippetChooserBlock('v1.Contact')), ('has_top_rule_line', wagtail.core.blocks.BooleanBlock(default=False, help_text='Add a horizontal rule line to top of contact block.', required=False))])), ('rss_feed', v1.atomic_elements.molecules.RSSFeed()), ('social_media', wagtail.core.blocks.StructBlock([('is_share_view', wagtail.core.blocks.BooleanBlock(default=True, help_text='If unchecked, social media icons will link users to official CFPB accounts. Do not fill in any further fields.', label='Desired action: share this page', required=False)), ('blurb', wagtail.core.blocks.CharBlock(default="Look what I found on the CFPB's site!", help_text='Sets the tweet text, email subject line, and LinkedIn post text.', required=False)), ('twitter_text', wagtail.core.blocks.CharBlock(help_text='(Optional) Custom text for Twitter shares. If blank, will default to value of blurb field above.', max_length=100, required=False)), ('twitter_related', wagtail.core.blocks.CharBlock(help_text='(Optional) A comma-separated list of accounts related to the content of the shared URL. Do not enter the  @ symbol. If blank, it will default to just "cfpb".', required=False)), ('twitter_hashtags', wagtail.core.blocks.CharBlock(help_text='(Optional) A comma-separated list of hashtags to be appended to default tweet text.', required=False)), ('twitter_lang', wagtail.core.blocks.CharBlock(help_text='(Optional) Loads text components in the specified language, if other than English. E.g., use "es"  for Spanish. See https://dev.twitter.com/web/overview/languages for a list of supported language codes.', required=False)), ('email_title', wagtail.core.blocks.CharBlock(help_text='(Optional) Custom subject for email shares. If blank, will default to value of blurb field above.', required=False)), ('email_text', wagtail.core.blocks.CharBlock(help_text='(Optional) Custom text for email shares. If blank, will default to "Check out this page from the CFPB".', required=False)), ('email_signature', wagtail.core.blocks.CharBlock(help_text='(Optional) Adds a custom signature line to email shares. ', required=False)), ('linkedin_title', wagtail.core.blocks.CharBlock(help_text='(Optional) Custom title for LinkedIn shares. If blank, will default to value of blurb field above.', required=False)), ('linkedin_text', wagtail.core.blocks.CharBlock(help_text='(Optional) Custom text for LinkedIn shares.', required=False))])), ('reusable_text', v1.blocks.ReusableTextChooserBlock(v1.models.snippets.ReusableText))], blank=True),
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='sidebar',
            field=wagtail.core.fields.StreamField([('call_to_action', wagtail.core.blocks.StructBlock([('slug_text', wagtail.core.blocks.CharBlock(required=False)), ('paragraph_text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('aria_label', wagtail.core.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('large', 'Large Primary')]))]))])), ('related_links', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('aria_label', wagtail.core.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False))])))])), ('related_metadata', wagtail.core.blocks.StructBlock([('slug', wagtail.core.blocks.CharBlock(max_length=100)), ('content', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100)), ('blob', wagtail.core.blocks.RichTextBlock())], icon='pilcrow')), ('list', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('aria_label', wagtail.core.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False))])))], icon='list-ul')), ('date', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100)), ('date', wagtail.core.blocks.DateBlock())], icon='date')), ('topics', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Topics', max_length=100)), ('show_topics', wagtail.core.blocks.BooleanBlock(default=True, required=False))], icon='tag'))])), ('is_half_width', wagtail.core.blocks.BooleanBlock(default=False, required=False))])), ('email_signup', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Stay informed', required=False)), ('default_heading', wagtail.core.blocks.BooleanBlock(default=True, help_text='If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', label='Default heading style', required=False)), ('text', wagtail.core.blocks.CharBlock(help_text='Write a sentence or two about what kinds of emails the user is signing up for, how frequently they will be sent, etc.', required=False)), ('signup_method', wagtail.core.blocks.ChoiceBlock(choices=[('form', 'Enter an email address directly in a form'), ('link', 'Link to a GovDelivery signup page')], help_text='Choose how people will sign up: either by entering their email directly or by going to a GovDelivery signup page', label='Signup method')), ('gd_code', wagtail.core.blocks.CharBlock(help_text='For a signup form, GovDeliery code (USCFPB_###) for the list people who submit the form will sign up for. For a signup link, URL for the GovDelivery signup page.', label='GovDelivery code or signup page URL', required=False)), ('disclaimer_page', wagtail.core.blocks.PageChooserBlock(help_text='Choose the page that the "See Privacy Act statement" link should go to. If in doubt, use "Generic Email Sign-Up Privacy Act Statement".', label='Privacy Act statement', required=False))])), ('reusable_text', v1.blocks.ReusableTextChooserBlock(v1.models.snippets.ReusableText))], blank=True),
        ),
    ]
