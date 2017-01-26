# -*- coding: utf-8 -*-
from setuptools import setup

with open('README.rst') as file:
    readme = read_data = file.read()

setup(name='clr',
      packages=['clr'],
      version='1.0.3',
      author='lmittmann',
      description='🌈 Terminal string styling',
      long_description=readme,
      keywords=[','.join(['clr', 'color', 'ansi', 'terminal styling', 'chalk'])],
      url='https://github.com/lmittmann/clr',
      license='MIT')
