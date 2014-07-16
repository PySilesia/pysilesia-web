PySilesia Project
=================

Installation
============

Project uses buildout (http://buildout.org)

1. python bootstrap.py
2. bin/buildout -c development.cfg / production.cfg # depending on environment
3. You need to set env variable DATABASE_URL = postgres://USER:PASSWORD@HOST:PORT/NAME
4. and other env variables (see in settings.py and production.py)
5. bin/django syncdb
6. bin/django migrate
7. bin/django runserver
