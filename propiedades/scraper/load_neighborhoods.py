#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simple module to load neighborhoods shapefile into the Django database.

It must be ran from the project directory and from the django shell. It will
take data from a shapefile and use it to populate the neighborhoods table.

Example:
    python manage.py shell   # open the shell
    from scraper import load_neighborhoods
    load_neighborhoods.main()

This doesn't need to be done unless neighborhoods information change. There is
a fixture with this data called "fixtures/initial_data.json". The following
should be ran from the command line to populate database using this fixture.

Example:
    python manage.py loaddata scraper/fixtures/initial_data.json
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import os

from django.contrib.gis.utils import LayerMapping
from scraper.models import Neighborhood

NEIHBORHOODS_SHP = "scraper/barrios_censo_2010/barrios_censo_2010.shp"


def main():
    shp_path = os.path.join(NEIHBORHOODS_SHP)
    mapping = {"name": "BARRIOS", "poly": "POLYGON"}
    lm = LayerMapping(Neighborhood, shp_path, mapping)
    lm.save(verbose=True)

if __name__ == '__main__':
    main()
