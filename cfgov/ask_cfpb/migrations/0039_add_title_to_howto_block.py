# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-05 20:39
from __future__ import unicode_literals

import v1.atomic_elements.organisms
import wagtail.core.blocks
import wagtail.core.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask_cfpb', '0038_recreated2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerpage',
            name='answer_content',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'link', 'ol', 'ul', 'document-link', 'image', 'embed'], label='Text'))])), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('tip', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(features=['link', 'document-link'], label='Tip'))])), ('video_player', wagtail.core.blocks.StructBlock([('video_url', wagtail.core.blocks.RegexBlock(default='https://www.youtube.com/embed/', error_messages={'invalid': 'The YouTube URL is in the wrong format. You must use the embed URL (https://www.youtube.com/embed/video_id), which can be obtained by clicking Share > Embed on the YouTube video page.', 'required': 'The YouTube URL field is required for video players.'}, label='YouTube Embed URL', regex='^https:\\/\\/www\\.youtube\\.com\\/embed\\/.+$', required=True))])), ('how_to_schema', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=500)), ('description', wagtail.core.blocks.RichTextBlock(blank=True, features=['ol', 'ul', 'bold', 'italic', 'link', 'document-link'], required=False)), ('steps', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=500)), ('step_content', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h3', 'link', 'ol', 'ul', 'document-link', 'image', 'embed'], label='Text'))])), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('tip', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(features=['link', 'document-link'], label='Tip'))])), ('video_player', wagtail.core.blocks.StructBlock([('video_url', wagtail.core.blocks.RegexBlock(default='https://www.youtube.com/embed/', error_messages={'invalid': 'The YouTube URL is in the wrong format. You must use the embed URL (https://www.youtube.com/embed/video_id), which can be obtained by clicking Share > Embed on the YouTube video page.', 'required': 'The YouTube URL field is required for video players.'}, label='YouTube Embed URL', regex='^https:\\/\\/www\\.youtube\\.com\\/embed\\/.+$', required=True))]))]))])))])), ('faq_schema', wagtail.core.blocks.StructBlock([('description', wagtail.core.blocks.RichTextBlock(blank=True, features=['ol', 'ul', 'bold', 'italic', 'link', 'document-link'], required=False)), ('questions', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('question', wagtail.core.blocks.CharBlock(max_length=500)), ('answer_content', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h3', 'link', 'ol', 'ul', 'document-link', 'image', 'embed'], label='Text'))])), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('tip', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(features=['link', 'document-link'], label='Tip'))])), ('video_player', wagtail.core.blocks.StructBlock([('video_url', wagtail.core.blocks.RegexBlock(default='https://www.youtube.com/embed/', error_messages={'invalid': 'The YouTube URL is in the wrong format. You must use the embed URL (https://www.youtube.com/embed/video_id), which can be obtained by clicking Share > Embed on the YouTube video page.', 'required': 'The YouTube URL field is required for video players.'}, label='YouTube Embed URL', regex='^https:\\/\\/www\\.youtube\\.com\\/embed\\/.+$', required=True))]))]))])))]))], blank=True, verbose_name='Answer'),
        ),
    ]
