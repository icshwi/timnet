#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import os
from setuptools import setup


# Read function
def safe_read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ""

# Setup
setup(name="python-timnet",
      version="0.0.1",
      description="MRF hardware based network toolkit",
      author="Jerzy Jamroz",
      author_email="jerzy.jamroz@gmail.com",
      license="GPLv2",
      url="",
      long_description=safe_read("README.md"),
      packages=['timnet'],
      #test_suite="nose.collector",
      )
