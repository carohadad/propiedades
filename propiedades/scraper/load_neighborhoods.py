#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simple module to load neighborhoods shapefile into the Django database.

It must be ran from the project directory.
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import os

from django.contrib.gis.utils import LayerMapping
from scraper.models import Neighborhood


def main():
    shp_path = os.path.join("scraper/barrios_censo_2010",
                            "barrios_censo_2010.shp")
    mapping = {"name": "BARRIOS", "poly": "POLYGON"}
    lm = LayerMapping(Neighborhood, shp_path, mapping)
    lm.save(verbose=True)

if __name__ == '__main__':
    main()
