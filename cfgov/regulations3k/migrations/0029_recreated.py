# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-12-16 12:41

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [
        ('regulations3k', '0001_initial'),
    ]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EffectiveVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authority', models.CharField(blank=True, max_length=255)),
                ('source', models.CharField(blank=True, max_length=255)),
                ('effective_date', models.DateField(default=datetime.date.today)),
                ('created', models.DateField(default=datetime.date.today)),
                ('draft', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['effective_date'],
                'default_related_name': 'version',
            },
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cfr_title_number', models.CharField(max_length=255)),
                ('chapter', models.CharField(max_length=255)),
                ('part_number', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('short_name', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'ordering': ['part_number'],
            },
        ),
    ]
