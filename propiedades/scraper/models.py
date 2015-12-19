""" Database Models for Scrapers.

This module contains the database models used by the different scrapers.

Models:
    SaleListing & RentListing: Both of them have the same properties but they
        have different behavior.
    Neighborhood: Neighborhood of the default city where properties can be
        located.
"""

from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models as gismodels


class Neighborhood(gismodels.Model):
    """Neighborhoods model."""

    name = gismodels.CharField(max_length=255, primary_key=True)
    poly = gismodels.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return "Name: {}".format(self.name)


class CommonListing(models.Model):
    """Properties model."""
    CURRENCIES = (
        ('ARS', 'Pesos Argentinos'),
        ('USD', 'Dolares'),
    )

    price = models.BigIntegerField()
    currency = models.CharField(max_length=3, choices=CURRENCIES)
    surface = models.IntegerField()
    rooms = models.IntegerField()
    address = models.CharField(max_length=255)

    class Meta:
        abstract = True


class SaleListing(CommonListing):
    pass


class RentListing(CommonListing):
    pass
