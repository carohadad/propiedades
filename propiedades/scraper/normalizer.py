#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Normalize input coming from the scrapers.

This module expose methods to normalize scraped fields from properties
websites, including geolocating tasks.
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import os


def normalize_address(address):
    """Normalize written address, together with geolocating tasks.

    Args:
        address (str): Written address like 'Sucre 3073'.

    Returns:
        tuple: Normalized address, coordinates, neighborhood and status.

        Example: (
            "Mariscal Antonio José de Sucre 3073, C1428DWC CABA, Argentina",
            [-34.5677463, -58.461533],
            "Belgrano",
            "OK"
            )
    """
    normalized_address, coordinates, status = geocode_address(address)

    if status == "OK":
        neighborhood = get_neighborhood(coordinates)
    else:
        neighborhood = None

    return normalized_address, coordinates, neighborhood, status


def geocode_address(address):
    pass


def get_neighborhood(coordinates):
    pass
