
# -*- coding: utf-8 -*-
import os

from aldryn_client import forms


class Form(forms.BaseForm):
    def to_settings(self, data, settings):
        
        from oscar import OSCAR_MAIN_TEMPLATE_DIR
        import oscar.defaults
        
        # Need to detect if these settings are for Django 1.8+
        # Is there a better way? Can't import django to check version =(
        is_django_18_or_later = ('TEMPLATES' in settings)
        
        
        # import all of Oscar's default settings
        settings.update(vars(oscar.defaults))
        
        # ------- TEMPLATES --------
        if is_django_18_or_later:
            
            settings['TEMPLATES'][0]['DIRS'].append(oscar.OSCAR_MAIN_TEMPLATE_DIR)
            # settings['TEMPLATES'][0]['APP_DIRS'] = True
            settings['TEMPLATES'][0]['OPTIONS']['context_processors'].extend([
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',                
            ])
        
        else:
            
            settings['TEMPLATE_CONTEXT_PROCESSORS'].extend([
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',                
                
            ])
            settings['TEMPLATE_DIRS'].append(oscar.OSCAR_MAIN_TEMPLATE_DIR)
            

        # ------- INSTALLED_APPS --------
        
        # flatpages could be installed by other applications, so check before adding it
        if not 'django.contrib.flatpages' in settings['INSTALLED_APPS']:
             settings['INSTALLED_APPS'].append('django.contrib.flatpages')
            
        settings['INSTALLED_APPS'].extend([
            'widget_tweaks'  # this is optional as far as Oscar is concerned
            ] + oscar.get_core_apps()
        )

        # ------- MIDDLEWARE --------

        settings['MIDDLEWARE_CLASSES'].extend([
            'oscar.apps.basket.middleware.BasketMiddleware',
        ])

        # flatpages could be configured by other applications, so check first
        if not 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware' in settings['MIDDLEWARE_CLASSES']:
             settings['MIDDLEWARE_CLASSES'].append('django.contrib.flatpages.middleware.FlatpageFallbackMiddleware')


        # ------- Other settings --------

        settings['AUTHENTICATION_BACKENDS'].append('oscar.apps.customer.auth_backends.EmailBackend')
        
        # need to check this
        settings['HAYSTACK_CONNECTIONS'] = {
            'default': {
                'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
            },
        }
        
        # ------- URLs --------
        settings['ADDON_URLS'].append('aldryn_django_oscar.urls')

        return settings
        