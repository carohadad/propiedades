""" Database Models for Propiedades.

This module contains the database models used by the different scrapers.

Models:
    SaleListing & RentListing: Both of them have the same properties but they
    have different behavior.


"""

from __future__ import unicode_literals

from django.db import models


class CommonListing(models.Model):
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
