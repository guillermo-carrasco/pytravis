from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pytravis',
      version=version,
      description="Python wrapper for Travis-CI API",
      long_description="""\
Python wrapper for Travis-CI API. Set of scripts to get information from travis.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='travis ci countinuous-integration api',
      author='Guillermo Carrasco Hernandez',
      author_email='guillermo.carrasco@scilifelab.se',
      url='http://guillermo-carrasco.github.com/pytravis/',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'requests'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
