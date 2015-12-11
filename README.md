Scraper de precios de inmuebles.
===

Tecnologías:
* Python
* Scrapy
* Docker
* Django
* nose
* pylint
* postgresql

Diariamente se scrapean los datos de alquiler y venta de inmuebles de la CABA, se guardan un una db y se realiza un analisis para la detección de outliers.

Los usarios pueden: 

* Darse de alta y configurar sus preferencias para recibir alertas dentro de su barrio/intereses particulares y dentro de un rango de precios
* Recibir avisos de unidades por debajo del valor de mercado para un perfil particular.

Instalacion:

- Instalar Python 2.7
- pip install django
- brew install postgresql
(para verificar que postgre funciona se puede correr psql -d postgres)

Instalar el adapter para django
- pip install psycopg2

En la carpeta del proyecto:
- python manage.py migrate

Para probar si esta todo configurado bien correr:
$ python manage.py dbshell


