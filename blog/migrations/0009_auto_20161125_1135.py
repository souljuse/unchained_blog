# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-25 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_category_category_post_user'),
    ]

    operations = [
        
        migrations.RenameField(
            model_name='category_post',
            old_name='text',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='category_post',
            name='created_date',
        ),
    ]
