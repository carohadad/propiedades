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

from geocoders import UsigGeocoder


class UsigGeocoderTestCase(unittest.TestCase):
    """Tests for UsigGeocoder class."""

    def test_normalize_and_geocode(self):
        address = "Sucre 3073"
        city = "Ciudad Autonoma de Buenos Aires"
        country = "Argentina"

        res = UsigGeocoder.normalize_and_geocode(address, city, country)
        exp = ("Sucre, Antonio Jose De, Mcal. 3073, " +
               "Ciudad Autonoma de Buenos Aires, Argentina",
               ['-34.567685', '-58.461493'],
               "OK")

        self.assertEqual(res, exp)


if __name__ == '__main__':
    nose.run(defaultTest=__name__)
