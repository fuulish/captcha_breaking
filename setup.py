#!/usr/bin/env python

from setuptools import setup

setup(name='aps_captcha',
      version='0.1',
      description='algorithm to automatically crack APS captcha',
      url='',
      author='Frank Uhlig',
      author_email='uhlig.frank@gmail.com',
      license='GPLv3',
      packages=['mlc'],
      scripts=[
          'scripts/crop_images.py',
          'scripts/prep_data.py',
          'scripts/trainNpredict.py',
          ],
      zip_safe=False)

