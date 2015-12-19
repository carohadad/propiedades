#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_geocoders.py

Tests for `geocoders.py` module.
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import unittest
import nose

from geocoders import UsigGeocoder, GoogleGeocoder, UnableToGeocode


class BaseGeocoderTestCase(unittest.TestCase):
    """Basic parameters for all geocoder tests."""

    def setUp(self):
        self.address = "Sucre 3073"
        self.city = "Ciudad Autonoma de Buenos Aires"
        self.country = "Argentina"


class UsigGeocoderTestCase(BaseGeocoderTestCase):
    """Tests for UsigGeocoder class."""

    def test_normalize_and_geocode(self):
        res = UsigGeocoder.normalize_and_geocode(self.address, self.city,
                                                 self.country)
        exp = ("Sucre, Antonio Jose De, Mcal. 3073, " +
               "Ciudad Autonoma de Buenos Aires, Argentina",
               ['-34.567685', '-58.461493'],
               "OK")

        self.assertEqual(res, exp)

    def test_unable_to_geocode(self):
        """Test that UsigGeocoder doesn't accept invalid input."""

        with self.assertRaises(UnableToGeocode):
            address = "Sucre"
            UsigGeocoder.normalize_and_geocode(address, self.city,
                                               self.country)

        with self.assertRaises(UnableToGeocode):
            address = "3073"
            UsigGeocoder.normalize_and_geocode(address, self.city,
                                               self.country)

        with self.assertRaises(UnableToGeocode):
            address = "3073 Sucre"
            UsigGeocoder.normalize_and_geocode(address, self.city,
                                               self.country)

        with self.assertRaises(UnableToGeocode):
            address = "Non existent street 4076"
            UsigGeocoder.normalize_and_geocode(address, self.city,
                                               self.country)


class GoogleGeocoderTestCase(BaseGeocoderTestCase):
    """Tests for GoogleGeocoder class."""

    def test_normalize_and_geocode(self):
        address = "Sucre 3073"
        city = "Ciudad Autonoma de Buenos Aires"
        country = "Argentina"

        res = GoogleGeocoder.normalize_and_geocode(address, city, country)
        exp = ("Mariscal Antonio José de Sucre 3073, C1428DWC CABA, Argentina",
               ["-34.5677463", "-58.461533"],
               "OK")

        self.assertEqual(res, exp)

    def test_unable_to_geocode(self):
        """Test that GoogleGeocoder throw exception if address not exists."""

        with self.assertRaises(UnableToGeocode):
            address = "xxxxxxxxxxxdlasjdfadkfjalsdfja"
            GoogleGeocoder.normalize_and_geocode(address, self.city,
                                                 self.country)

if __name__ == '__main__':
    nose.run(defaultTest=__name__)
