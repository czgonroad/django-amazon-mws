django-amazon-mws
=================

Django integration with Amazon MWS.

Getting started
===============

Install the package with ``pip``.

``$ pip install django-amazon-mws``

Add the application to your ``INSTALLED_APPS``

.. code:: python

   INSTALLED_APPS = [
       ...,
       'djmws',
   ]

Development
===========

Clone this repo, make a virtual environment then install the package + dev and documentation dependencies straight from the repo itself.

``$ pip install -e .[dev, docs]``

From within the `docs/` directory, you can run the following to get a live reloading server serving the HTML documentation at `http://127.0.0.1:8000`.

``$ sphinx-autobuild . _build/html/``