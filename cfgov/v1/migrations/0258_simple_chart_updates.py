# Generated by Django 2.2.23 on 2021-06-03 15:58

import django.core.validators
import jobmanager.blocks
import v1.atomic_elements.organisms
import v1.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0257_add_story_page_with_image_bleeding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browsepage',
            name='content',
            field=wagtail.core.fields.StreamField([('full_width_text', wagtail.core.blocks.StreamBlock([('content', wagtail.core.blocks.RichTextBlock(icon='edit')), ('content_with_anchor', wagtail.core.blocks.StructBlock([('content_block', wagtail.core.blocks.RichTextBlock()), ('anchor_link', wagtail.core.blocks.StructBlock([('link_id', wagtail.core.blocks.CharBlock(help_text='\n            ID will be auto-generated on save.\n            However, you may enter some human-friendly text that\n            will be incorporated to make it easier to read.\n        ', label='ID for this content block', required=False))]))])), ('heading', wagtail.core.blocks.StructBlock([('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.core.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], required=False)), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.core.blocks.StructBlock([('upload', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.core.blocks.CharBlock(help_text="If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), ('image_width', wagtail.core.blocks.ChoiceBlock(choices=[('full', 'Full width'), (470, '470px'), (270, '270px'), (170, '170px'), ('bleed', 'Bleed into left/right margins')])), ('image_position', wagtail.core.blocks.ChoiceBlock(choices=[('right', 'right'), ('left', 'left')], help_text='Does not apply if the image is full-width')), ('text', wagtail.core.blocks.RichTextBlock(label='Caption', required=False)), ('is_bottom_rule', wagtail.core.blocks.BooleanBlock(default=True, help_text='Check to add a horizontal rule line to bottom of inset.', label='Has bottom rule line', required=False))])), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('quote', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.TextBlock()), ('citation', wagtail.core.blocks.TextBlock(required=False)), ('is_large', wagtail.core.blocks.BooleanBlock(required=False))])), ('cta', wagtail.core.blocks.StructBlock([('slug_text', wagtail.core.blocks.CharBlock(required=False)), ('paragraph_text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('large', 'Large Primary')]))]))])), ('related_links', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False))])))])), ('reusable_text', v1.blocks.ReusableTextChooserBlock('v1.ReusableText')), ('email_signup', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Stay informed', required=False)), ('default_heading', wagtail.core.blocks.BooleanBlock(default=True, help_text='If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', label='Default heading style', required=False)), ('text', wagtail.core.blocks.CharBlock(help_text='Write a sentence or two about what kinds of emails the user is signing up for, how frequently they will be sent, etc.', required=False)), ('gd_code', wagtail.core.blocks.CharBlock(help_text='Code for the topic (i.e., mailing list) you want people who submit this form to subscribe to. Format: USCFPB_###', label='GovDelivery code', required=False)), ('disclaimer_page', wagtail.core.blocks.PageChooserBlock(help_text='Choose the page that the "See Privacy Act statement" link should go to. If in doubt, use "Generic Email Sign-Up Privacy Act Statement".', label='Privacy Act statement', required=False))])), ('well', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(label='Well', required=False))])), ('well_with_ask_search', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(label='Well', required=False)), ('ask_search', wagtail.core.blocks.StructBlock([('show_label', wagtail.core.blocks.BooleanBlock(default=True, help_text='Whether to show form label.', required=False)), ('placeholder', wagtail.core.blocks.TextBlock(help_text='Text to show for the input placeholder text.', required=False))]))]))])), ('info_unit_group', wagtail.core.blocks.StructBlock([('format', wagtail.core.blocks.ChoiceBlock(choices=[('50-50', '50/50'), ('33-33-33', '33/33/33'), ('25-75', '25/75')], help_text='Choose the number and width of info unit columns.', label='Format')), ('heading', wagtail.core.blocks.StructBlock([('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.core.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], required=False)), ('intro', wagtail.core.blocks.RichTextBlock(help_text='If this field is not empty, the Heading field must also be set.', required=False)), ('link_image_and_heading', wagtail.core.blocks.BooleanBlock(default=True, help_text="Check this to link all images and headings to the URL of the first link in their unit's list, if there is a link.", required=False)), ('has_top_rule_line', wagtail.core.blocks.BooleanBlock(default=False, help_text='Check this to add a horizontal rule line to top of info unit group.', required=False)), ('lines_between_items', wagtail.core.blocks.BooleanBlock(default=False, help_text='Check this to show horizontal rule lines between info units.', label='Show rule lines between items', required=False)), ('info_units', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.core.blocks.StructBlock([('upload', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.core.blocks.CharBlock(help_text="If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), ('heading', wagtail.core.blocks.StructBlock([('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.core.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], default={'level': 'h3'}, required=False)), ('body', wagtail.core.blocks.RichTextBlock(blank=True, required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False))]), required=False))]))), ('sharing', wagtail.core.blocks.StructBlock([('shareable', wagtail.core.blocks.BooleanBlock(help_text='If checked, share links will be included below the items.', label='Include sharing links?', required=False)), ('share_blurb', wagtail.core.blocks.CharBlock(help_text='Sets the tweet text, email subject line, and LinkedIn post text.', required=False))]))])), ('simple_chart', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('subtitle', wagtail.core.blocks.TextBlock(required=False)), ('description', wagtail.core.blocks.TextBlock(help_text='Accessible description of the chart content', required=True)), ('figure_number', wagtail.core.blocks.CharBlock(required=False)), ('chart_type', wagtail.core.blocks.ChoiceBlock(choices=[('bar', 'Bar'), ('datetime', 'Datetime'), ('line', 'Line'), ('tilemap', 'Tilemap')])), ('data_source', wagtail.core.blocks.TextBlock(help_text="URL of the chart's data source or an array of JSON data", required=True)), ('data_series', wagtail.core.blocks.TextBlock(help_text='A list of column headers (CSV) or keys (JSON) to include as data in the chart in the format [<key>, <key>, <key>]. Other labels may be included via: {"key": <key>, "label": <label>}', required=False)), ('x_axis_source', wagtail.core.blocks.TextBlock(help_text='The column header (CSV), key or data array (JSON) to include as the source of x-axis values.', required=False)), ('y_axis_label', wagtail.core.blocks.CharBlock(help_text='y-axis label', required=False)), ('x_axis_label', wagtail.core.blocks.CharBlock(help_text='x-axis label, if needed', required=False)), ('transform', wagtail.core.blocks.CharBlock(help_text='Name of the javascript function in chart-hooks.js to run on the provided data before handing it to the chart', required=False)), ('filters', wagtail.core.blocks.CharBlock(help_text='Array of JSON objects of the form {"key": <key>, "label": <label>} to filter the underlying chart data on', required=False)), ('style_overrides', wagtail.core.blocks.TextBlock(help_text='A JSON object with style overrides for the underlying Highcharts chart. No object merging is done, nested objects should be referenced with dot notation: {"tooltip.shape": "circle"}', required=False)), ('credits', wagtail.core.blocks.CharBlock(help_text='Attribution for the data source', required=False)), ('date_published', wagtail.core.blocks.CharBlock(help_text='When the underlying data was published', required=False)), ('download_file', wagtail.core.blocks.CharBlock(help_text='Location of a file to download, if different from the data source', required=False)), ('download_text', wagtail.core.blocks.CharBlock(help_text='Custom text for the chart download field', required=False)), ('notes', wagtail.core.blocks.TextBlock(help_text='General chart information', required=False))])), ('expandable_group', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(help_text='Added as an <code>&lt;h3&gt;</code> at the top of this block. Also adds a wrapping <code>&lt;div&gt;</code> whose <code>id</code> attribute comes from a slugified version of this heading, creating an anchor that can be used when linking to this part of the page.', required=False)), ('body', wagtail.core.blocks.RichTextBlock(required=False)), ('is_accordion', wagtail.core.blocks.BooleanBlock(required=False)), ('has_top_rule_line', wagtail.core.blocks.BooleanBlock(default=False, help_text='Check this to add a horizontal rule line to top of expandable group.', required=False)), ('expandables', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('is_bordered', wagtail.core.blocks.BooleanBlock(required=False)), ('is_midtone', wagtail.core.blocks.BooleanBlock(required=False)), ('is_expanded', wagtail.core.blocks.BooleanBlock(required=False)), ('content', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('well', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(label='Well', required=False))])), ('links', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False))])), ('email', wagtail.core.blocks.StructBlock([('emails', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.EmailBlock(label='Email address')), ('text', wagtail.core.blocks.CharBlock(label='Link text (optional)', required=False))])))])), ('phone', wagtail.core.blocks.StructBlock([('fax', wagtail.core.blocks.BooleanBlock(default=False, label='Is this number a fax?', required=False)), ('phones', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('number', wagtail.core.blocks.CharBlock(help_text='Do not include spaces or dashes. Ex. 8554112372', max_length=15, validators=[django.core.validators.RegexValidator(message='Enter a numeric phone number, without punctuation.', regex='^\\d*$')])), ('extension', wagtail.core.blocks.CharBlock(max_length=4, required=False)), ('vanity', wagtail.core.blocks.CharBlock(help_text='A phoneword version of the above number. Include any formatting. Ex. (555) 222-CFPB', max_length=15, required=False)), ('tty', wagtail.core.blocks.CharBlock(help_text='Do not include spaces or dashes. Ex. 8554112372', label='TTY', max_length=15, required=False, validators=[django.core.validators.RegexValidator(message='Enter a numeric phone number, without punctuation.', regex='^\\d*$')])), ('tty_ext', wagtail.core.blocks.CharBlock(label='TTY Extension', max_length=4, required=False))])))])), ('address', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(required=False)), ('street', wagtail.core.blocks.CharBlock(required=False)), ('city', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('state', wagtail.core.blocks.CharBlock(max_length=25, required=False)), ('zip_code', wagtail.core.blocks.CharBlock(max_length=15, required=False))]))], blank=True))])))])), ('expandable', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('is_bordered', wagtail.core.blocks.BooleanBlock(required=False)), ('is_midtone', wagtail.core.blocks.BooleanBlock(required=False)), ('is_expanded', wagtail.core.blocks.BooleanBlock(required=False)), ('content', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('well', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(label='Well', required=False))])), ('links', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False))])), ('email', wagtail.core.blocks.StructBlock([('emails', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.EmailBlock(label='Email address')), ('text', wagtail.core.blocks.CharBlock(label='Link text (optional)', required=False))])))])), ('phone', wagtail.core.blocks.StructBlock([('fax', wagtail.core.blocks.BooleanBlock(default=False, label='Is this number a fax?', required=False)), ('phones', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('number', wagtail.core.blocks.CharBlock(help_text='Do not include spaces or dashes. Ex. 8554112372', max_length=15, validators=[django.core.validators.RegexValidator(message='Enter a numeric phone number, without punctuation.', regex='^\\d*$')])), ('extension', wagtail.core.blocks.CharBlock(max_length=4, required=False)), ('vanity', wagtail.core.blocks.CharBlock(help_text='A phoneword version of the above number. Include any formatting. Ex. (555) 222-CFPB', max_length=15, required=False)), ('tty', wagtail.core.blocks.CharBlock(help_text='Do not include spaces or dashes. Ex. 8554112372', label='TTY', max_length=15, required=False, validators=[django.core.validators.RegexValidator(message='Enter a numeric phone number, without punctuation.', regex='^\\d*$')])), ('tty_ext', wagtail.core.blocks.CharBlock(label='TTY Extension', max_length=4, required=False))])))])), ('address', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(required=False)), ('street', wagtail.core.blocks.CharBlock(required=False)), ('city', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('state', wagtail.core.blocks.CharBlock(max_length=25, required=False)), ('zip_code', wagtail.core.blocks.CharBlock(max_length=15, required=False))]))], blank=True))])), ('well', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(label='Well', required=False))])), ('video_player', wagtail.core.blocks.StructBlock([('video_id', wagtail.core.blocks.RegexBlock(error_messages={'invalid': 'The YouTube video ID is in the wrong format.'}, help_text='Enter the YouTube video ID, which is located at the end of the video URL, after "v=". For example, the video ID for https://www.youtube.com/watch?v=1V0Ax9OIc84 is 1V0Ax9OIc84.', label='YouTube video ID', regex='^[\\w-]{11}$', required=False)), ('thumbnail_image', wagtail.images.blocks.ImageChooserBlock(help_text='Optional thumbnail image to show before and after the video plays. If the thumbnail image is not set here, the video player will default to showing the thumbnail that was set in (or automatically chosen by) YouTube.', required=False))])), ('snippet_list', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock(required=False)), ('has_top_rule_line', wagtail.core.blocks.BooleanBlock(default=False, help_text='Check this to add a horizontal rule line above this block.', required=False)), ('image', wagtail.core.blocks.StructBlock([('upload', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.core.blocks.CharBlock(help_text="If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), ('actions_column_width', wagtail.core.blocks.ChoiceBlock(choices=[('70', '70%'), ('66', '66%'), ('60', '60%'), ('50', '50%'), ('40', '40%'), ('33', '33%'), ('30', '30%')], help_text='Choose the width in % that you wish to set the Actions column in a resource list.', label='Width of "Actions" column', required=False)), ('show_thumbnails', wagtail.core.blocks.BooleanBlock(help_text="If selected, each resource in the list will include a 150px-wide image from the resource's thumbnail field.", required=False)), ('actions', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link_label', wagtail.core.blocks.CharBlock(help_text='E.g., "Download" or "Order free prints"')), ('snippet_field', wagtail.core.blocks.ChoiceBlock(choices=[('related_file', 'Related file'), ('alternate_file', 'Alternate file'), ('link', 'Link'), ('alternate_link', 'Alternate link')], help_text='The field that the action link should point to'))]))), ('tags', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Tag'), help_text='Enter tag names to filter the snippets. For a snippet to match and be output in the list, it must have been tagged with all of the tag names listed here. The tag names are case-insensitive.'))])), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('feedback', wagtail.core.blocks.StructBlock([('was_it_helpful_text', wagtail.core.blocks.CharBlock(default='Was this page helpful to you?', help_text='Use this field only for feedback forms that use "Was this helpful?" radio buttons.', required=False)), ('intro_text', wagtail.core.blocks.CharBlock(help_text='Optional feedback intro', required=False)), ('question_text', wagtail.core.blocks.CharBlock(help_text='Optional expansion on intro', required=False)), ('radio_intro', wagtail.core.blocks.CharBlock(help_text='Leave blank unless you are building a feedback form with extra radio-button prompts, as in /owning-a-home/help-us-improve/.', required=False)), ('radio_text', wagtail.core.blocks.CharBlock(default='This information helps us understand your question better.', required=False)), ('radio_question_1', wagtail.core.blocks.CharBlock(default='How soon do you expect to buy a home?', required=False)), ('radio_question_2', wagtail.core.blocks.CharBlock(default='Do you currently own a home?', required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Submit')), ('contact_advisory', wagtail.core.blocks.RichTextBlock(help_text='Use only for feedback forms that ask for a contact email', required=False))])), ('raw_html_block', wagtail.core.blocks.RawHTMLBlock(label='Raw HTML block')), ('conference_registration_form', wagtail.core.blocks.StructBlock([('govdelivery_code', wagtail.core.blocks.CharBlock(help_text='Conference registrants will be subscribed to this GovDelivery topic.', label='GovDelivery code')), ('govdelivery_question_id', wagtail.core.blocks.RegexBlock(error_messages={'invalid': 'GovDelivery question ID must be 5 digits.'}, help_text='Enter the ID of the question in GovDelivery that is being used to track registration for this conference. It is the number in the question URL, e.g., the <code>12345</code> in <code>https://admin.govdelivery.com/questions/12345/edit</code>.', label='GovDelivery question ID', regex='^\\d{5,}$', required=False)), ('govdelivery_answer_id', wagtail.core.blocks.RegexBlock(error_messages={'invalid': 'GovDelivery answer ID must be 5 digits.'}, help_text='Enter the ID of the affirmative answer for the above question. To find it, right-click on the answer in the listing on a page like <code>https://admin.govdelivery.com/questions/12345/answers</code>, inspect the element, and look around in the source for a five-digit ID associated with that answer. <strong>Required if Govdelivery question ID is set.</strong>', label='GovDelivery answer ID', regex='^\\d{5,}$', required=False)), ('capacity', wagtail.core.blocks.IntegerBlock(help_text='Enter the (physical) conference attendance limit as a number.')), ('success_message', wagtail.core.blocks.RichTextBlock(help_text='Enter a message that will be shown on successful registration.')), ('at_capacity_message', wagtail.core.blocks.RichTextBlock(help_text='Enter a message that will be shown when the event is at capacity.')), ('failure_message', wagtail.core.blocks.RichTextBlock(help_text='Enter a message that will be shown if the GovDelivery subscription fails.'))])), ('chart_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('chart_type', wagtail.core.blocks.ChoiceBlock(choices=[('bar', 'Bar | % y-axis values'), ('line', 'Line | millions/billions y-axis values'), ('line-index', 'Line-Index | integer y-axis values'), ('tile_map', 'Tile Map | grid-like USA map')])), ('color_scheme', wagtail.core.blocks.ChoiceBlock(choices=[('blue', 'Blue'), ('gold', 'Gold'), ('green', 'Green'), ('navy', 'Navy'), ('neutral', 'Neutral'), ('purple', 'Purple'), ('teal', 'Teal')], help_text='Chart\'s color scheme. See "https://github.com/cfpb/cfpb-chart-builder#createchart-options-".', required=False)), ('data_source', wagtail.core.blocks.CharBlock(help_text='Location of the chart\'s data source relative to "https://files.consumerfinance.gov/data/". For example,"consumer-credit-trends/auto-loans/num_data_AUT.csv".', required=True)), ('date_published', wagtail.core.blocks.DateBlock(help_text='Automatically generated when CCT cron job runs')), ('description', wagtail.core.blocks.CharBlock(help_text='Briefly summarize the chart for visually impaired users.', required=True)), ('has_top_rule_line', wagtail.core.blocks.BooleanBlock(default=False, help_text='Check this to add a horizontal rule line to top of chart block.', required=False)), ('last_updated_projected_data', wagtail.core.blocks.DateBlock(help_text='Month of latest entry in dataset')), ('metadata', wagtail.core.blocks.CharBlock(help_text='Optional metadata for the chart to use. For example, with CCT this would be the chart\'s "group".', required=False)), ('note', wagtail.core.blocks.CharBlock(help_text='Text to display as a footnote. For example, "Data from the last six months are not final."', required=False)), ('y_axis_label', wagtail.core.blocks.CharBlock(help_text='Custom y-axis label. NOTE: Line-Index chart y-axis is not overridable with this field!', required=False))])), ('mortgage_chart_block', wagtail.core.blocks.StructBlock([('content_block', wagtail.core.blocks.RichTextBlock()), ('title', wagtail.core.blocks.CharBlock(form_classname='title', required=True)), ('description', wagtail.core.blocks.CharBlock(help_text='Chart summary for visually impaired users.', required=False)), ('note', wagtail.core.blocks.CharBlock(help_text='Text for "Note" section of footnotes.', required=False)), ('has_top_rule_line', wagtail.core.blocks.BooleanBlock(default=False, help_text='Check this to add a horizontal rule line to top of chart block.', required=False))])), ('mortgage_map_block', wagtail.core.blocks.StructBlock([('content_block', wagtail.core.blocks.RichTextBlock()), ('title', wagtail.core.blocks.CharBlock(form_classname='title', required=True)), ('description', wagtail.core.blocks.CharBlock(help_text='Chart summary for visually impaired users.', required=False)), ('note', wagtail.core.blocks.CharBlock(help_text='Text for "Note" section of footnotes.', required=False)), ('has_top_rule_line', wagtail.core.blocks.BooleanBlock(default=False, help_text='Check this to add a horizontal rule line to top of chart block.', required=False))])), ('mortgage_downloads_block', wagtail.core.blocks.StructBlock([('show_archives', wagtail.core.blocks.BooleanBlock(default=False, help_text='Check this box to allow the archival section to display. No section will appear if there are no archival downloads.', required=False))])), ('data_snapshot', wagtail.core.blocks.StructBlock([('market_key', wagtail.core.blocks.CharBlock(help_text='Market identifier, e.g. AUT', max_length=20, required=True)), ('num_originations', wagtail.core.blocks.CharBlock(help_text='Number of originations, e.g. 1.2 million', max_length=20)), ('value_originations', wagtail.core.blocks.CharBlock(help_text='Total dollar value of originations, e.g. $3.4 billion', max_length=20)), ('year_over_year_change', wagtail.core.blocks.CharBlock(help_text='Percentage change, e.g. 5.6% increase', max_length=20)), ('last_updated_projected_data', wagtail.core.blocks.DateBlock(help_text='Month of latest entry in dataset')), ('num_originations_text', wagtail.core.blocks.CharBlock(help_text='Descriptive sentence, e.g. Auto loans originated', max_length=100)), ('value_originations_text', wagtail.core.blocks.CharBlock(help_text='Descriptive sentence, e.g. Dollar volume of new loans', max_length=100)), ('year_over_year_change_text', wagtail.core.blocks.CharBlock(help_text='Descriptive sentence, e.g. In year-over-year originations', max_length=100)), ('inquiry_month', wagtail.core.blocks.DateBlock(help_text='Month of latest entry in dataset for inquiry data', max_length=20, required=False)), ('inquiry_year_over_year_change', wagtail.core.blocks.CharBlock(help_text='Percentage change, e.g. 5.6% increase', max_length=20, required=False)), ('inquiry_year_over_year_change_text', wagtail.core.blocks.CharBlock(help_text='Descriptive sentence, e.g. In year-over-year inquiries', max_length=100, required=False)), ('tightness_month', wagtail.core.blocks.DateBlock(help_text='Month of latest entry in dataset for credit tightness data', max_length=20, required=False)), ('tightness_year_over_year_change', wagtail.core.blocks.CharBlock(help_text='Percentage change, e.g. 5.6% increase', max_length=20, required=False)), ('tightness_year_over_year_change_text', wagtail.core.blocks.CharBlock(help_text='Descriptive sentence, e.g. In year-over-year credit tightness', max_length=100, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image', required=False))])), ('job_listing_table', jobmanager.blocks.JobListingTable()), ('yes_checklist', wagtail.core.blocks.StructBlock([('checklist', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('item', wagtail.core.blocks.CharBlock(help_text='Short description for a checkbox item')), ('details', wagtail.core.blocks.RichTextBlock(help_text='Deeper explanation of the item', required=False))])))]))], blank=True),
        ),
    ]
