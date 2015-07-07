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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255, help_text='Enter name of the author')),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('bookCode', models.CharField(max_length=255, help_text='Enter code of the book. use UPPERCASE')),
                ('department', models.CharField(max_length=255, help_text='Specify the department. Use UPPERCASE')),
                ('shelve', models.CharField(max_length=255, help_text='Specify the shelve')),
            ],
        ),
        migrations.CreateModel(
            name='Main_table',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255, help_text='Enter title of a book')),
                ('year_pb', models.CharField(max_length=255, help_text='Enter published year of a book')),
                ('rfid', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='Image_books/')),
                ('author', models.ForeignKey(to='catalog.Authors')),
                ('location', models.ForeignKey(to='catalog.Locations')),
            ],
        ),
    ]
