#!/usr/bin/env python

from setuptools import setup

setup(name='ftw',
      version='1.2.0',
      description='Framework for Testing WAFs',
      author='Chaim Sanders, Zack Allen',
      author_email='zma4580@gmail.com, chaim.sanders@gmail.com',
      url='https://www.github.com/crs-support/ftw',
      download_url='https://github.com/crs-support/ftw/tarball/1.2.0',
      include_package_data=True,
      package_data={
          'ftw': ['util/public_suffix_list.dat']
      },
      entry_points={
          'pytest11': [
              'ftw = ftw.pytest_plugin'
          ]
      },
      packages=['ftw'],
      keywords=['waf'],
      install_requires=[
          'Brotli==1.0.7',
          'IPy==0.83',
          'PyYAML==4.2b1',
          'pytest==4.6',
          'python-dateutil==2.6.0',
          'six==1.14.0'
      ])
