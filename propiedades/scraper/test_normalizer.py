#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_normalizer.py

Tests for `normalizer.py` module.
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import unittest
import nose
from mock import Mock

import normalizer
import load_neighborhoods
import geocoders


class NormalizerTestCase(unittest.TestCase):
    """Tests for normalizer methods."""

    def set_neighborhoods_db(self):
        """Helper method to load neighborhoods in the db model."""
        load_neighborhoods.main()

    # @unittest.skip("skip")
    def test_normalize_address(self):
        """High level mocked test of the normalize_address method."""
        normalizer.geocode_address = Mock(return_value=(
            "Mariscal Antonio José de Sucre 3073, C1428DWC CABA, Argentina",
            [-34.5677463, -58.461533],
            "OK"))

        normalizer.get_neighborhood = Mock(return_value="Belgrano")

        res = normalizer.normalize_address("Sucre 3073")
        exp = (
            "Mariscal Antonio José de Sucre 3073, C1428DWC CABA, Argentina",
            [-34.5677463, -58.461533],
            "Belgrano",
            "OK"
        )

        self.assertEqual(res, exp)

    # @unittest.skip("skip")
    def test_geocode_address(self):
        """Test method that use geocoder objects to geocode.

        Used a mock geocoder object, the idea is not to test geocoders (that is
        done in test_geocoders module, but to test the higher level function.
        """

        exp = (
            "Mariscal Antonio José de Sucre 3073, C1428DWC CABA, Argentina",
            [-34.5677463, -58.461533],
            "OK"
        )

        class MockGeocoder(object):
            """Mock geocoder that returns expected output."""

            @classmethod
            def normalize_and_geocode(cls, address, city, country):
                return exp

        geocoders.get = Mock(return_value=[MockGeocoder])

        res = normalizer.geocode_address("Sucre 3073")

        self.assertEqual(res, exp)

    # @unittest.skip("skip")
    def test_get_neighborhood(self):
        """Test neighborhood assigning from coordinates."""
        self.set_neighborhoods_db()

        res = normalizer.get_neighborhood([-34.5677463, -58.461533])
        exp = "Belgrano"

        self.assertEqual(res, exp)

if __name__ == '__main__':
    nose.run(defaultTest=__name__)
