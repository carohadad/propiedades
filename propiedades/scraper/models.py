"""Models for the scraper"""

from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models as gismodels


class Neighborhood(gismodels.Model):
    """Neighborhoods where properties could be."""
    name = gismodels.CharField(max_length=255, primary_key=True)
    poly = gismodels.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return "Name: {}".format(self.name)
