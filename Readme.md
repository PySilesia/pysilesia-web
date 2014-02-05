PySilesia Project
=================

Installation
============

Project uses buildout (http://buildout.org)

1. python bootstrap.py
2. bin/buildout -c development.cfg / production.cfg # depending on environment
3. configure environment variables (see in settings.py and production.py)
4. bin/django syncdb
5. bin/django migrate
6. bin/django runserver
