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
