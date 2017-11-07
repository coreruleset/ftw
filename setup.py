#!/usr/bin/env python

from setuptools import setup

setup(name='ftw',
      version='1.1.5',
      description='Framework for Testing WAFs',
      author='Chaim Sanders, Zack Allen',
      author_email='zma4580@gmail.com, chaim.sanders@gmail.com',
      url='https://www.github.com/crs-support/ftw',
      download_url='https://github.com/crs-support/ftw/tarball/1.1.5',
      include_package_data=True,
      package_data={
        'ftw': ['util/public_suffix_list.dat']
      },
      entry_points = {
        'pytest11': [
            'ftw = ftw.pytest_plugin'
        ]
      },
      packages=['ftw'],
      keywords=['waf'],
      install_requires=[
          'IPy',
          'pytest==2.9.1',
          'PyYAML',
          'python-dateutil==2.6.0'
      ],
     )
