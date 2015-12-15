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

import geocoder

DEFAULT_CITY = "Ciudad Autonoma de Buenos Aires"
DEFAULT_COUNTRY = "Argentina"


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
    """Geocode written address.

    Args:
        address (str): Written address like 'Sucre 3073'.

    Returns:
        tuple: Normalized address, coordinates and status.

        Example: (
            "Mariscal Antonio José de Sucre 3073, C1428DWC CABA, Argentina",
            [-34.5677463, -58.461533],
            "OK"
            )
    """
    g = geocoder.google(_prenormalize_address(address))

    if g.status == "OK":
        normalized_address = g.address.decode("utf-8")
        coordinates = g.latlng
        status = g.status

    else:
        normalized_address, coordinates = None, None
        status = g.status

    return normalized_address, coordinates, status


def _prenormalize_address(address):
    """Prenormalize address to maximize geocoding success probability."""
    return ", ".join([address, DEFAULT_CITY, DEFAULT_COUNTRY])


def get_neighborhood(coordinates):
    pass
