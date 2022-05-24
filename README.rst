**Deprecated**

This project is no longer supported.

Divio will undertake no further development or maintenance of this project. If you are interested in continuing to 
develop it, use the fork functionality from GitHub. We are not able to transfer ownership of the repository to another 
party.

Aldryn Django Oscar
===================

Aldryn Django Oscar is a simple wrapper around django-oscar to easily install the package on Aldryn Cloud.

Oscar is an e-commerce framework for Django designed for building domain-driven sites. It is structured such that any part of the core functionality can be customised to suit the needs of your project. This allows a wide range of e-commerce requirements to be handled, from large-scale B2C sites to complex B2B sites rich in domain-specific business logic.

Key settings
------------

``ALDRYN_DJANGO_OSCAR_URL_PREFIX`` (defaults to ``shop``): the URL prefix for Oscar views.

See this addon's URL patterns for how this is used: https://github.com/aldryn/aldryn-django-oscar/blob/master/aldryn_django_oscar/urls_i18n.py.
