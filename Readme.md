PySilesia Project
=================

Installation
============

Project uses buildout (http://buildout.org)

1. python bootstrap.py
2. bin/buildout -c <environment>.cfg
3. You need to set env variable DATABASE_URL = postgres://USER:PASSWORD@HOST:PORT/NAME
4. bin/django syncdb
5. bin/django migrate
6. bin/django runserver
