# Generated by Django 2.2.16 on 2021-03-17 16:03

import wagtail.core.blocks
import wagtail.core.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers_digital_platform', '0024_add_notification_type_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityindexpage',
            name='header',
            field=wagtail.core.fields.StreamField([('text_introduction', wagtail.core.blocks.StructBlock([('eyebrow', wagtail.core.blocks.CharBlock(help_text='Optional: Adds an H5 eyebrow above H1 heading text. Only use in conjunction with heading.', label='Pre-heading', required=False)), ('heading', wagtail.core.blocks.CharBlock(required=False)), ('intro', wagtail.core.blocks.RichTextBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock(required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False))]), required=False)), ('has_rule', wagtail.core.blocks.BooleanBlock(help_text='Check this to add a horizontal rule line to bottom of text introduction.', label='Has bottom rule', required=False))])), ('notification', wagtail.core.blocks.StructBlock([('type', wagtail.core.blocks.ChoiceBlock(choices=[('information', 'Information'), ('warning', 'Warning')])), ('message', wagtail.core.blocks.CharBlock(help_text='The main notification message to display.', required=True)), ('explanation', wagtail.core.blocks.TextBlock(help_text='Explanation text appears below the message in smaller type.', required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False))]), help_text='Links appear on their own lines below the explanation.', required=False))]))], blank=True),
        ),
    ]
