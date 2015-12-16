Scraper de precios de inmuebles.
===

[![Coverage Status](https://coveralls.io/repos/chadad/propiedades/badge.svg?branch=master&service=github)](https://coveralls.io/github/chadad/propiedades?branch=master)
[![Build Status](https://travis-ci.org/chadad/propiedades.svg)](https://travis-ci.org/chadad/propiedades)
[![Stories in Ready](https://badge.waffle.io/chadad/propiedades.png?label=ready&title=ReadyToWork)](https://waffle.io/chadad/propiedades)

## Tecnologías
* Python
* Scrapy
* Docker
* Django
* nose
* flake8 
* postgresql

Diariamente se scrapean los datos de alquiler y venta de inmuebles de la CABA, se guardan un una db y se realiza un analisis para la detección de outliers.

## Los usarios pueden

* Darse de alta y configurar sus preferencias para recibir alertas dentro de su barrio/intereses particulares y dentro de un rango de precios
* Recibir avisos de unidades por debajo del valor de mercado para un perfil particular.

## Instalación

- Instalar Python 2.7
- `brew install gdal`
- `brew install postgresql`
(para verificar que postgre funciona se puede correr psql -d postgres)
- `brew install psycopg2` o `fink install psycopg2-py27` o `sudo port install py27-psycopg2`
- `pip install -r requirements.txt`

Correr las migraciones y popular la base de barrios
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py loaddata scraper/fixtures/initial_data.json`

Para probar si esta todo configurado bien correr: `python manage.py dbshell`

*Posibles errores y su solución*

Si en Mac ocurre el error:
```
django.core.exceptions.ImproperyConfigured: Error loading psycop2 module
Library not loaded: libssl.1.0.0.dylib
Referenced from: .../psycopg2/_psycopg.so
Reason: image not found
```

Se debe correr en la línea de comandos:
```
sudo ln -s /Applications/Postgres.app/Contents/Versions/9.5/lib/libssl.1.0.0.dylib /usr/local/lib/

sudo ln -s /Applications/Postgres.app/Contents/Versions/9.5/lib/libcrypto.1.0.0.dylib /usr/local/lib/
```

Donde */Applications/Postgres.app/Contents/Versions/9.5* es el path y la versión donde está instalado Postgres; también podría estar en un path como */Library/PosgreSQL/9.4* o en otro lugar.

Para encontrar el path adecuado puede ser útil correr `locate libssl` en la línea de comandos y buscar aquel path donde está instalado Postgres que contiene los archivos **libssl.1.0.0.dylib** y **libcrypto.1.0.0.dylib**

Algunos OS X pueden requerir realizar el symlink en `/usr/lib` pero otros no permiten la operación y debe realizarse en `/usr/local/lib`.

## Convenciones de estilo
Este proyecto sigue las convenciones de la [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

Ver un ejemplo completo del [uso de docstrings en python según la guía de Google](http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google)

*Linting en Sublime Text*

Instalar los siguientes paquetes con el package manager.

* **Anaconda**
* **PEP8 Autoformat**: Setear las preferencias con `"autoformat_on_save": true`

*Snippets en Sublime Text*

1. Tools > New Snippet
2. Copiar y pegar contenido

    * [pyscript](snippets/pyscript.sublime-snippet): Tipear *pyscript* en un nuevo archivo para cargar un template de módulo en python.
    * [testmodule](snippets/testmodule.sublime-snippet): Tipear *testmodule* en un nuevo archivo para cargar un template de módulo de testing en python.

Paquete de snippets: **Sublime Text 3 Snippets** o **Sublime Text 2 Snippets**

## Tests

Para correr los tests: `python manage.py test`

Para crear tests, debe tenerse en cuenta que hay que usar la clase `django.test.TestCase` en lugar de `unittest.TestCase`, ya que incluye un manejo automático de la base de datos para testeos.






