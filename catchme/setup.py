#!/usr/bin/python3

"""
Setup file for Skeleton
"""
try:
  from setuptools import setup
except ImportError:
  from distutils.com import setup

config = {
  'description': 'AI program to demostrate field transversal ',
  'author': 'Benjamin Lehman',
  'URL' : 'https://github.com/milarepa/catchme',
  'download URL': 'https://github.com/milarepa/catchme',
  'author email': 'your email',
  'version': '0.1',
  'install requires': ['nose'],
  'packages': ['catchme'],
  'scripts': [],
  'name': 'catchme'
  }

  setup(**config)
