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
* pyflakes 
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

Instalar los siguientes paquetes con el package manager.

* **Anaconda**:
* **PEP8 Autoformat**: Setear las preferencias con `"autoformat_on_save": true`

*Snippets en Sublime Text*

1. Tools > New Snippet
2. Copiar y pegar contenido

    * [pyscript](snippets/pyscript.sublime-snippet): Tipear *pyscript* en un nuevo archivo para cargar un template de módulo en python.
    * [testmodule](snippets/testmodule.sublime-snippet): Tipear *testmodule* en un nuevo archivo para cargar un template de módulo de testing en python.

Paquete de snippets: **Sublime Text 3 Snippets** o **Sublime Text 2 Snippets**

*Tests*

Para correr los tests:

python manage.py test




