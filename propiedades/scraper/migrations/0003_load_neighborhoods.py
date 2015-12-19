# -*- coding: utf-8 -*-

"""
Populate database with neighborhood initial data.

This is custom user migration that loads neighborhood data into the database
created in the previous migration. It uses the load_neighborhoods module to
read a shapefile and populate the neighborhoods table with it.

The procedure of populating a django database using empty migrations can be
summarized in these steps:
    1. python manage.py makemigrations --empty <yourapp> --name initial_data
    2. Edit migration file adding a method that takes *apps* and
        *schema_editor* variables, and populate the database, as shown below.
"""

from __future__ import unicode_literals
from django.db import migrations

from scraper import load_neighborhoods


def load_initial_data(apps, schema_editor):
    load_neighborhoods.main()


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_data)
    ]
