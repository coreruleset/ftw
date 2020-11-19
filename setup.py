#!/usr/bin/env python

from setuptools import setup

setup(name='ftw',
      version='1.3.0',
      description='Framework for Testing WAFs',
      author='Chaim Sanders, Zack Allen',
      author_email='zma4580@gmail.com, chaim.sanders@gmail.com',
      url='https://www.github.com/coreruleset/ftw',
      download_url='https://github.com/coreruleset/ftw/tarball/1.2.2',
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
      # custom PyPI classifier for pytest plugins
      classifiers=["Framework :: Pytest"],
      install_requires=[
          'Brotli==1.0.9',
          'IPy==1.00',
          'PyYAML==5.3.1',
          'pytest==6.1.2',
          'python-dateutil==2.8.1',
      ])
