# -*- coding: utf-8 -*-
import os

from aldryn_client import forms


class Form(forms.BaseForm):
    def to_settings(self, data, settings):
        from oscar import defaults
        from oscar import OSCAR_MAIN_TEMPLATE_DIR, get_core_apps
        settings.update(vars(defaults))
        settings['INSTALLED_APPS'].extend(
            ['django.contrib.flatpages',
             'widget_tweaks'
             ] + get_core_apps()
        )
        settings['TEMPLATES'] = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [
                    os.path.join(settings['BASE_DIR'], 'templates'),
                    OSCAR_MAIN_TEMPLATE_DIR
                ],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',

                        'oscar.apps.search.context_processors.search_form',
                        'oscar.apps.promotions.context_processors.promotions',
                        'oscar.apps.checkout.context_processors.checkout',
                        'oscar.apps.customer.notifications.context_processors.notifications',
                        'oscar.core.context_processors.metadata',
                    ],
                },
            },
        ]
        settings['MIDDLEWARE_CLASSES'].extend([
            'oscar.apps.basket.middleware.BasketMiddleware',
            'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
        ])
        settings['AUTHENTICATION_BACKENDS'] = (
            'oscar.apps.customer.auth_backends.EmailBackend',
            'django.contrib.auth.backends.ModelBackend',
        )
        settings['HAYSTACK_CONNECTIONS'] = {
            'default': {
                'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
            },
        }
        settings['ADDON_URLS'].append('aldryn_django_oscar.urls')
        return settings
        