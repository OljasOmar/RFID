# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('author_id', models.CharField(max_length=255)),
                ('author_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('bookCode', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('shelve', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Main_table',
            fields=[
                ('id', models.CharField(serialize=False, max_length=255, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('author_name_id', models.CharField(max_length=255)),
                ('year_pb', models.CharField(max_length=255)),
                ('location_id', models.CharField(max_length=255)),
                ('rfid', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='Image_books/')),
            ],
        ),
    ]
