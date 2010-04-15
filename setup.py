#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Seg 14 Set 2009 14:42:06 CEST 

"""Installation instructions for django-ordered-model
"""

from setuptools import setup, find_packages

setup(

    name = 'django-order',
    version = '0.1.2',
    packages = find_packages(),

    # we also need all translation files and templates
    package_data = {
      'order': [
        'media/img/*.png',
        'locale/*/LC_MESSAGES/django.po',
        'locale/*/LC_MESSAGES/django.mo',
        ],
      },

    entry_points = {
      },

    zip_safe=False,

    install_requires = [
      'Django>=1.1',
      'docutils',
      ],

    # metadata for upload to PyPI
    author = 'André Anjos',
    author_email = "andre.dos.anjos@gmail.com",
    description = 'Defines a model that has an order',
    license = "GPL v2 or superior",
    keywords = "django model order",
    url = 'http://andreanjos.org/project/django-order/',
)
