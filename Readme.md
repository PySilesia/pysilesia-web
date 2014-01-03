PySilesia Project
=================

Installation
============

Project uses buildout (http://buildout.org)

1. python bootstrap.py
2. bin/buildout -c development.cfg / production.cfg # depending on environment
3. bin/django syncdb
4. bin/django migrate
5. bin/django runserver
