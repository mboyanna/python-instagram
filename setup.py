#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="python-instagram",
      version="1.3.2.1",
      description="Instagram API client",
      license="MIT",
      install_requires=["simplejson","httplib2","six"],
      author="Instagram, Inc",
      author_email="apidevelopers@instagram.com",
      url="https://github.com/mboyanna/python-instagram.git",
      packages = find_packages(),
      keywords= "instagram",
      zip_safe = True)
