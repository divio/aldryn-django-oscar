# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, include

from oscar.app import application


prefix = getattr(
    settings,
    'ALDRYN_DJANGO_OSCAR_URL_PREFIX',
    'shop',
)

if prefix:
    prefix = r'{}/'.format(prefix)

urlpatterns = [
    url(prefix, include(application.urls)),
]
