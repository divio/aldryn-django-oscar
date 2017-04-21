# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from aldryn_django_oscar import __version__

REQUIREMENTS = [
    'aldryn-django',
    'django-oscar==1.2.2',
]

setup(
    name='aldryn-django-oscar',
    version=__version__,
    description=open('README.rst').read(),
    author='Divio AG',
    author_email='info@divio.com',
    url='https://github.com/django-oscar/django-oscar',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=REQUIREMENTS,
    include_package_data=True,
    zip_safe=False,
)
