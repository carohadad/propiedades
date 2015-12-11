Scraper de precios de inmuebles.
===

## Tecnologías
* Python
* Scrapy
* Docker
* Django
* nose
* pylint

Diariamente se scrapean los datos de alquiler y venta de inmuebles de la CABA, se guardan un una db y se realiza un analisis para la detección de outliers.

## Los usarios pueden

* Darse de alta y configurar sus preferencias para recibir alertas dentro de su barrio/intereses particulares y dentro de un rango de precios
* Recibir avisos de unidades por debajo del valor de mercado para un perfil particular.

## Instalación

- Instalar Python 2.7
- `brew install psycopg2`
- `pip install -r requirements.txt`

## Convención de estilo
Este proyecto sigue las convenciones de la [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

Ver un ejemplo completo del [uso de docstrings en python según la guía de Google](http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google)

*Linting en Sublime Text*
* **Anaconda**: Setear las preferencias con `"use_pylint": true`
* **PEP8 Autoformat**: Setear las preferencias con `"autoformat_on_save": true`



