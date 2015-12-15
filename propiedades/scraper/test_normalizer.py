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


class NormalizerTestCase(unittest.TestCase):
    """Tests for normalizer methods."""

    def set_neighborhoods_db(self):
        load_neighborhoods.main()

    def test_normalize_address(self):
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

    @unittest.skip("skip")
    def test_geocode_address(self):
        res = normalizer.geocode_address("Sucre 3073")
        exp = (
            "Mariscal Antonio José de Sucre 3073, C1428DWC CABA, Argentina",
            [-34.5677463, -58.461533],
            "OK"
        )

        self.assertEqual(res, exp)

    def test_get_neighborhood(self):
        self.set_neighborhoods_db()

        res = normalizer.get_neighborhood([-34.5677463, -58.461533])
        exp = "Belgrano"

        self.assertEqual(res, exp)

if __name__ == '__main__':
    nose.run(defaultTest=__name__)
