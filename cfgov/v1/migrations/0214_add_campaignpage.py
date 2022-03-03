# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-06 21:31
from __future__ import unicode_literals

import django.db.models.deletion
import v1.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0213_abstracthero_and_add_jumbohero'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignPage',
            fields=[
                ('cfgovpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='v1.CFGOVPage')),
                ('header', wagtail.core.fields.StreamField([('hero', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(help_text='For complete guidelines on creating heroes, visit our <a href="https://cfpb.github.io/design-system/components/heroes">Design System</a>. Character counts (including spaces) at largest breakpoint:<ul class="help">    <li>&bull; 41 characters max (one-line heading)</li>    <li>&bull; 82 characters max (two-line heading)</li></ul>', required=False)), ('body', wagtail.core.blocks.RichTextBlock(help_text='Character counts (including spaces) at largest breakpoint:<ul class="help">    <li>&bull; 165-186 characters (after a one-line heading)</li>    <li>&bull; 108-124 characters (after a two-line heading)</li></ul>', label='Sub-heading', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='When saving illustrations, use a transparent background. <a href="https://cfpb.github.io/design-system/components/heroes#style">See image dimension guidelines.</a>', label='Large image', required=False)), ('small_image', wagtail.images.blocks.ImageChooserBlock(help_text='<b>Optional.</b> Provides an alternate image for small displays when using a photo or bleeding hero. Not required for the standard illustration. <a href="https://cfpb.github.io/design-system/components/heroes#style">See image dimension guidelines.</a>', required=False)), ('background_color', wagtail.core.blocks.CharBlock(help_text='Specify a hex value (including the # sign) from our <a href="https://cfpb.github.io/design-manual/brand-guidelines/color-principles.html">official color palette</a>.', required=False)), ('is_white_text', wagtail.core.blocks.BooleanBlock(help_text='<b>Optional.</b> Turns the hero text white. Useful if using a dark background color or background image.', label='White text', required=False)), ('is_overlay', wagtail.core.blocks.BooleanBlock(help_text='<b>Optional.</b> Uses the large image as a background under the entire hero, creating the "Photo" style of hero (see <a href="https://cfpb.github.io/design-system/components/heroes">Design System</a> for details). When using this option, make sure to specify a background color (above) for the left/right margins that appear when screens are wider than 1200px and for the text section when the photo and text stack at mobile sizes.', label='Photo', required=False)), ('is_bleeding', wagtail.core.blocks.BooleanBlock(help_text='<b>Optional.</b> Select if you want the illustration to bleed vertically off the top and bottom of the hero space.', label='Bleed', required=False))])), ('jumbo_hero', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(help_text='For complete guidelines on creating heroes, visit our <a href="https://cfpb.github.io/design-system/components/heroes">Design System</a>. Character counts (including spaces) at largest breakpoint:<ul class="help">    <li>&bull; 41 characters max (one-line heading)</li>    <li>&bull; 82 characters max (two-line heading)</li></ul>', required=False)), ('body', wagtail.core.blocks.RichTextBlock(help_text='Character counts (including spaces) at largest breakpoint:<ul class="help">    <li>&bull; 165-186 characters (after a one-line heading)</li>    <li>&bull; 108-124 characters (after a two-line heading)</li></ul>', label='Sub-heading', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='When saving illustrations, use a transparent background. <a href="https://cfpb.github.io/design-system/components/heroes#style">See image dimension guidelines.</a>', label='Large image', required=False)), ('small_image', wagtail.images.blocks.ImageChooserBlock(help_text='<b>Optional.</b> Provides an alternate image for small displays when using a photo or bleeding hero. Not required for the standard illustration. <a href="https://cfpb.github.io/design-system/components/heroes#style">See image dimension guidelines.</a>', required=False)), ('background_color', wagtail.core.blocks.CharBlock(help_text='Specify a hex value (including the # sign) from our <a href="https://cfpb.github.io/design-manual/brand-guidelines/color-principles.html">official color palette</a>.', required=False)), ('is_white_text', wagtail.core.blocks.BooleanBlock(help_text='<b>Optional.</b> Turns the hero text white. Useful if using a dark background color or background image.', label='White text', required=False))])), ('features', wagtail.core.blocks.StructBlock([('format', wagtail.core.blocks.ChoiceBlock(choices=[('50-50', '50/50'), ('33-33-33', '33/33/33'), ('25-75', '25/75')], help_text='Choose the number and width of info unit columns.', label='Format')), ('heading', wagtail.core.blocks.StructBlock([('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.core.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#the-icons">See full list of icons</a>', required=False))], required=False)), ('intro', wagtail.core.blocks.RichTextBlock(help_text='If this field is not empty, the Heading field must also be set.', required=False)), ('link_image_and_heading', wagtail.core.blocks.BooleanBlock(default=True, help_text="Check this to link all images and headings to the URL of the first link in their unit's list, if there is a link.", required=False)), ('has_top_rule_line', wagtail.core.blocks.BooleanBlock(default=False, help_text='Check this to add a horizontal rule line to top of info unit group.', required=False)), ('lines_between_items', wagtail.core.blocks.BooleanBlock(default=False, help_text='Check this to show horizontal rule lines between info units.', label='Show rule lines between items', required=False)), ('info_units', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.core.blocks.StructBlock([('upload', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.core.blocks.CharBlock(help_text="If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), ('heading', wagtail.core.blocks.StructBlock([('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.core.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#the-icons">See full list of icons</a>', required=False))], default={'level': 'h3'}, required=False)), ('body', wagtail.core.blocks.RichTextBlock(blank=True, required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False))]), required=False))]))), ('sharing', wagtail.core.blocks.StructBlock([('shareable', wagtail.core.blocks.BooleanBlock(help_text='If checked, share links will be included below the items.', label='Include sharing links?', required=False)), ('share_blurb', wagtail.core.blocks.CharBlock(help_text='Sets the tweet text, email subject line, and LinkedIn post text.', required=False))]))]))], blank=True)),
                ('content', wagtail.core.fields.StreamField([('info_units', wagtail.core.blocks.StructBlock([('format', wagtail.core.blocks.ChoiceBlock(choices=[('50-50', '50/50'), ('33-33-33', '33/33/33'), ('25-75', '25/75')], help_text='Choose the number and width of info unit columns.', label='Format')), ('heading', wagtail.core.blocks.StructBlock([('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.core.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#the-icons">See full list of icons</a>', required=False))], required=False)), ('intro', wagtail.core.blocks.RichTextBlock(help_text='If this field is not empty, the Heading field must also be set.', required=False)), ('link_image_and_heading', wagtail.core.blocks.BooleanBlock(default=True, help_text="Check this to link all images and headings to the URL of the first link in their unit's list, if there is a link.", required=False)), ('has_top_rule_line', wagtail.core.blocks.BooleanBlock(default=False, help_text='Check this to add a horizontal rule line to top of info unit group.', required=False)), ('lines_between_items', wagtail.core.blocks.BooleanBlock(default=False, help_text='Check this to show horizontal rule lines between info units.', label='Show rule lines between items', required=False)), ('info_units', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.core.blocks.StructBlock([('upload', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.core.blocks.CharBlock(help_text="If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))])), ('heading', wagtail.core.blocks.StructBlock([('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.core.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#the-icons">See full list of icons</a>', required=False))], default={'level': 'h3'}, required=False)), ('body', wagtail.core.blocks.RichTextBlock(blank=True, required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False))]), required=False))]))), ('sharing', wagtail.core.blocks.StructBlock([('shareable', wagtail.core.blocks.BooleanBlock(help_text='If checked, share links will be included below the items.', label='Include sharing links?', required=False)), ('share_blurb', wagtail.core.blocks.CharBlock(help_text='Sets the tweet text, email subject line, and LinkedIn post text.', required=False))]))]))], blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('v1.cfgovpage',),
        ),
    ]
