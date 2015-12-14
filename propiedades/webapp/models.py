""" Models for the webapp
"""
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models


class Preferences(models.Model):
    """ Preferences for each User to be notified about Properties
    """
    user = models.ForeignKey(User)

    max_price = models.BigIntegerField()
    min_price = models.BigIntegerField()

    rooms = models.IntegerField(null=True)

    max_surface = models.BigIntegerField(null=True)
    min_surface = models.BigIntegerField(null=True)
