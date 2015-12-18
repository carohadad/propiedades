#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Geocoding strategies available to normalize and geocode addresses.

Expose a list of geocoding strategies with the same interface, ordered by
convenience. They must be iterated passing the same information until one of
them is able to deliver results.

Example:
    import geocoders
    for geocoder in geocoders.get():
        try:
            res = geocoder.normalize_and_geocode(address, city, country)
            break
    normalized_address, coordinates, status = res
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import os
import re
import json

import geocoder
import requests


# EXCEPTIONS
class UnableToGeocode(Exception):
    """Raises when a geocoder can't handle an address."""

    def __init__(self, address, city, country, geocoder_name):
        msg = " ".join(["Unable to geocode",
                        unicode(address), unicode(city), unicode(country),
                        "using", unicode(geocoder_name)])
        super(UnableToGeocode, self).__init__(msg)


# GEOCODERS
class BaseGeocoder(object):
    """Implements geocoders interface."""

    @classmethod
    def normalize_and_geocode(cls, address, city, country):
        """Normalize and geocode an address from a particular city-country.

        Args:
            address (str): Written address like 'Sucre 3073'.
            city (str): A city name like "Ciudad Autonoma de Buenos Aires".
            country (str): A country name like "Argentina".

        Returns:
            tuple: (normalized_address, coordinates, status)

            Example: (
                "Mariscal Antonio José de Sucre 3073, C1428DWC CABA,
                    Argentina",
                [-34.5677463, -58.461533],
                "OK")
        """
        return cls._normalize_and_geocode(address, city, country)

    @classmethod
    def _prenormalize_address(cls, address, city, country):
        """Prenormalize address to maximize geocoding success probability."""
        return ", ".join([address, city, country])


class GoogleGeocoder(BaseGeocoder):
    """Geocode using google API."""

    @classmethod
    def _normalize_and_geocode(cls, address, city, country):
        g = geocoder.google(cls._prenormalize_address(address, city, country))

        if g.status == "OK":
            normalized_address = g.address.decode("utf-8")
            coordinates = g.latlng
            status = g.status
            return normalized_address, coordinates, status

        else:
            raise UnableToGeocode(address, city, country, "Google")


class UsigGeocoder(BaseGeocoder):
    """Geocode using USIG web API.

    Only valid for "Ciudad Autonoma de Buenos Aires" city and "Argentina" cty.
    """
    BASE_URL = "http://ws.usig.buenosaires.gob.ar/rest"

    @classmethod
    def _normalize_and_geocode(cls, address, city, country):
        try:
            street, number = cls._read_address(address)
        except:
            raise UnableToGeocode(address, city, country, "Usig")

        res = cls._usig_geocode(street, number)

        # get address and coordinates
        normalization = res["Normalizacion"]
        gkba_geocoded = res["GeoCodificacion"]

        # parse normalized address
        res_address = normalization["DireccionesCalleAltura"]["direcciones"][0]
        norm_street = res_address["Calle"].decode("utf-8").title()
        norm_number = res_address["Altura"].decode("utf-8")
        normalized_address = ", ".join([norm_street + " " + norm_number,
                                        city, country]).strip()

        # convert coordinates
        coordinates = cls._usig_convert(gkba_geocoded["x"], gkba_geocoded["y"])

        g = geocoder.google(cls._prenormalize_address(address, city, country))

        return normalized_address, coordinates, "OK"

    @classmethod
    def _read_address(cls, address):
        return re.match("(\D+)\s*(\d+)", address, re.UNICODE).groups()

    @classmethod
    def _usig_geocode(cls, street, number):
        service = "normalizar_y_geocodificar_direcciones"
        url = cls.BASE_URL + "/" + service

        res = requests.get(url, params={
            "calle": street,
            "altura": number,
            "desambiguar": 1
        })

        return json.loads(res.content)

    @classmethod
    def _usig_convert(cls, x, y):
        service = "convertir_coordenadas"
        url = cls.BASE_URL + "/" + service

        res = requests.get(url, params={"x": x, "y": y, "output": "lonlat"})
        parsed_res = json.loads(res.content)

        return [parsed_res["resultado"]["y"], parsed_res["resultado"]["x"]]


def get():
    return [GoogleGeocoder, UsigGeocoder]
