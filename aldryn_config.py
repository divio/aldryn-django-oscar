
# -*- coding: utf-8 -*-
import os

from aldryn_client import forms


class Form(forms.BaseForm):
    def to_settings(self, data, settings):

        # import all of Oscar's default settings
        import oscar.defaults
        settings.update(vars(oscar.defaults))

        context_processors = [
            'oscar.apps.search.context_processors.search_form',
            'oscar.apps.promotions.context_processors.promotions',
            'oscar.apps.checkout.context_processors.checkout',
            'oscar.apps.customer.notifications.context_processors.notifications',
            'oscar.core.context_processors.metadata',
        ]

        # ------- TEMPLATES --------

        from oscar import OSCAR_MAIN_TEMPLATE_DIR

        new_style_template_setting = ('TEMPLATES' in settings)
        if new_style_template_setting:
            settings['TEMPLATES'][0]['DIRS'].append(OSCAR_MAIN_TEMPLATE_DIR)
            settings['TEMPLATES'][0]['OPTIONS']['context_processors'].extend(context_processors)
        else:
            settings['TEMPLATE_DIRS'].append(OSCAR_MAIN_TEMPLATE_DIR)
            settings['TEMPLATE_CONTEXT_PROCESSORS'].extend(context_processors)

        # ------- INSTALLED_APPS --------

        # flatpages could be installed by other applications, so check before adding it
        flatpages_app = 'django.contrib.flatpages'
        if flatpages_app not in settings['INSTALLED_APPS']:
            settings['INSTALLED_APPS'].append(flatpages_app)

        settings['INSTALLED_APPS'].extend([
            'widget_tweaks'  # this is optional as far as Oscar is concerned
            ] + oscar.get_core_apps()
        )

        # ------- MIDDLEWARE --------

        settings['MIDDLEWARE_CLASSES'].extend([
            'oscar.apps.basket.middleware.BasketMiddleware',
        ])

        # flatpages could be configured by other applications, so check first
        flatpages_middleware = 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
        if flatpages_middleware not in settings['MIDDLEWARE_CLASSES']:
            settings['MIDDLEWARE_CLASSES'].append(flatpages_middleware)

        # ------- Other settings --------

        settings['AUTHENTICATION_BACKENDS'].append('oscar.apps.customer.auth_backends.EmailBackend')

        haystack = 'HAYSTACK_CONNECTIONS'
        haystack_config = {'ENGINE': 'haystack.backends.simple_backend.SimpleEngine'}

        if haystack in settings:
            if 'default' not in settings[haystack]:
                settings[haystack]['default'] = haystack_config
        else:
            settings[haystack] = {
                'default': haystack_config
            }

        # ------- URLs --------

        settings['ADDON_URLS_I18N'].append('aldryn_django_oscar.urls_i18n')

        return settings
