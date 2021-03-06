# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year', models.PositiveIntegerField()),
                ('genres', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('fmt', models.CharField(max_length=20)),
                ('length', models.PositiveIntegerField()),
                ('url', models.URLField()),
                ('img', models.URLField()),
            ],
        ),
    ]
