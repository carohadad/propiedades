#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_models.py
Tests for `models.py` module.
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement

import nose
from nose.tools import raises

from django.test import TestCase
from django.core.exceptions import ValidationError

from models import SaleListing
from models import RentListing


class CommonListingTestCase(TestCase):
    """Tests for Listing classes."""

    def test_create_new_sale_listing(self):
        """ Tests SaleListing creation. """
        initial_count = len(SaleListing.objects.all())

        new_listing = SaleListing(
            price=123,
            currency='ARS',
            surface=40,
            rooms=2,
            address='Independencia 635')

        new_listing.full_clean()
        new_listing.save()

        self.assertEqual(len(SaleListing.objects.all()), initial_count + 1)

    def test_create_new_rent_listing(self):
        """ Tests RentListing creation. """
        initial_count = len(RentListing.objects.all())

        new_listing = RentListing(
            price=123,
            currency='ARS',
            surface=40,
            rooms=2,
            address='Independencia 635')

        new_listing.full_clean()
        new_listing.save()

        self.assertEqual(len(RentListing.objects.all()), initial_count + 1)

    @raises(ValidationError)
    def test_cannot_create_listing_with_invalid_currency(self):
        """ Tests Listing Validation. """

        new_listing = RentListing(
            price=123,
            currency='POP',
            surface=40,
            rooms=2,
            address='Independencia 635')

        new_listing.full_clean()


if __name__ == '__main__':
    nose.run(defaultTest=__name__)
