# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-30 07:19
from __future__ import unicode_literals

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_author_detail_introduction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author_detail',
            old_name='photo',
            new_name='photo1',
        ),
        migrations.RenameField(
            model_name='book_detail',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='author_detail',
            name='photo2',
            field=models.FileField(blank=True, null=True, upload_to=books.models.upload_location_authors),
        ),
        migrations.AddField(
            model_name='author_detail',
            name='photo3',
            field=models.FileField(blank=True, null=True, upload_to=books.models.upload_location_authors),
        ),
        migrations.AddField(
            model_name='book_detail',
            name='image2',
            field=models.FileField(blank=True, null=True, upload_to=books.models.upload_location_books),
        ),
        migrations.AddField(
            model_name='book_detail',
            name='image3',
            field=models.FileField(blank=True, null=True, upload_to=books.models.upload_location_books),
        ),
        migrations.AddField(
            model_name='book_detail',
            name='image4',
            field=models.FileField(blank=True, null=True, upload_to=books.models.upload_location_books),
        ),
        migrations.AddField(
            model_name='book_detail',
            name='image5',
            field=models.FileField(blank=True, null=True, upload_to=books.models.upload_location_books),
        ),
    ]