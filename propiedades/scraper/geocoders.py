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

To add a new geocoder:
    1. A new concrete class has to subclass BaseGeocoder implementing the
        private method used by the interface.
    2. The new geocoder class has to be added in the get() list, in the
        preferred priority order.
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import os
import re
import json

import geocoder
import requests
from unidecode import unidecode


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
        return cls._normalize_and_geocode(unidecode(address), city, country)

    @classmethod
    def _prenormalize_address(cls, address, city, country):
        """Prenormalize address to maximize geocoding success probability."""
        return ", ".join([address, city, country])


class GoogleGeocoder(BaseGeocoder):
    """Geocode using google API."""

    @classmethod
    def _normalize_and_geocode(cls, address, city, country):
        g = geocoder.google(cls._prenormalize_address(address, city, country))
        print(g.status, g.address, g.latlng)
        if g.status == "OK" and g.street:
            normalized_address = g.address.decode("utf-8")
            coordinates = [unicode(coord) for coord in g.latlng]
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

        if res["Normalizacion"]["TipoResultado"] != "DireccionNormalizada":
            raise UnableToGeocode(address, city, country, "Usig")

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
        """Separate street from number like in "Sucre 3073". """
        return re.match("(\D+)\s*(\d+)", address, re.UNICODE).groups()

    @classmethod
    def _usig_geocode(cls, street, number):
        """Geocode an address using USIG web API.
        Args:
            street (str): Street name like "Sucre".
            number (str): Address number like "3073".

        Returns:
            dict: Gecoded and normalized address.

            Example:
                {Normalizacion: {
                    TipoResultado: "DireccionNormalizada",
                    DireccionesCalleAltura: {
                        direcciones: [
                            {CodigoCalle: "20120",
                            Calle: "SUCRE, ANTONIO JOSE DE, MCAL.",
                            Altura: "3073"}
                            ]
                    },
                GeoCodificacion: {x: "100165.847714", y: "106831.897209"}
                }
        """
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
        """Convert gkba coordinates to regular geographical coordinates.

        Args:
            x, y (str): lon, lat in Gauss Kruegues Bs As projection.

        Returns:
            list: [lat, lon] in geographical coordinates.
        """
        service = "convertir_coordenadas"
        url = cls.BASE_URL + "/" + service

        res = requests.get(url, params={"x": x, "y": y, "output": "lonlat"})
        parsed_res = json.loads(res.content)

        return [parsed_res["resultado"]["y"], parsed_res["resultado"]["x"]]


def get():
    return [UsigGeocoder, GoogleGeocoder]
