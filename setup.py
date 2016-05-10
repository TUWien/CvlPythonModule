#!/usr/bin/env python

from distutils.core import setup

setup(name='Dummy Module',
      version='0.1.0',
      description='Python dummy module',
      author='Markus Diem',
      author_email='diem@caa.tuwien.ac.at',
      url='http://www.caa.tuwien.ac.at/cvl/',
      packages=['mymodule', 'test'],
      package_dir={'mymodule':  'lib/mymodule',
                   'test':      'lib/test'},
      package_data={'mymodule': ['data/*.dat']},
      )
