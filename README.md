Scraper de precios de inmuebles.
===

[![Coverage Status](https://coveralls.io/repos/chadad/propiedades/badge.svg?branch=master&service=github)](https://coveralls.io/github/chadad/propiedades?branch=master)
[![Build Status](https://travis-ci.org/chadad/propiedades.svg)](https://travis-ci.org/chadad/propiedades)

## Tecnologías
* Python
* Scrapy
* Docker
* Django
* nose
* pylint
* postgresql

Diariamente se scrapean los datos de alquiler y venta de inmuebles de la CABA, se guardan un una db y se realiza un analisis para la detección de outliers.

## Los usarios pueden

* Darse de alta y configurar sus preferencias para recibir alertas dentro de su barrio/intereses particulares y dentro de un rango de precios
* Recibir avisos de unidades por debajo del valor de mercado para un perfil particular.

## Instalación

- Instalar Python 2.7
- `brew install postgresql`
(para verificar que postgre funciona se puede correr psql -d postgres)
- `brew install psycopg2`
- `pip install -r requirements.txt`

Correr las migraciones
- python manage.py migrate

Para probar si esta todo configurado bien correr:
$ python manage.py dbshell

## Convención de estilo
Este proyecto sigue las convenciones de la [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

Ver un ejemplo completo del [uso de docstrings en python según la guía de Google](http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google)

*Linting en Sublime Text*
* **Anaconda**: Setear las preferencias con `"use_pylint": true`
* **PEP8 Autoformat**: Setear las preferencias con `"autoformat_on_save": true`





