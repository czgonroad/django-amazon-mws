django-amazon-mws
=================
.. image:: https://travis-ci.org/python-amazon-mws/django-amazon-mws.svg?branch=master

Django integration with Amazon MWS.

Supported Django versions:

- Django 1.11
- Django 2.0

Supported Python versions:

- Python 2.7
- Python 3.4
- Python 3.5
- Python 3.6

Getting started
===============

Install the package with ``pip``.

``$ pip install django-amazon-mws``

Add the application to your ``INSTALLED_APPS``.

.. code:: python

   INSTALLED_APPS = [
       ...,
       'djmws',
   ]

Add a ``DEFAULT_MARKETPLACE`` to your ``settings.py`` file.

.. code:: python

   DEFAULT_MARKETPLACE = 'UK'

Development
===========

Clone this repo, make a virtual environment then install the package + dev and documentation dependencies straight from the repo itself.

``$ pip install -e .[dev, docs]``

From within the ``docs/`` directory, you can run the following to get a live reloading server serving the HTML documentation at ``http://127.0.0.1:8000``.

``$ sphinx-autobuild . _build/html/``