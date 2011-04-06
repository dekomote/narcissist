#!/usr/bin/env python

from distutils.core import setup
import setuptools

setup(name='narcissist',
      version='0.1',
      description='Deployable personal info web app / web service aggregator.',
      author='Dejan Noveski',
      author_email='dr.mote@gmail.com',
      url='',
      packages=['narcissist'],
      install_requires=[
        "Flask>=0.7",
      ],
     )
