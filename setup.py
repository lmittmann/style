# -*- coding: utf-8 -*-
from setuptools import setup
from style import __version__


with open('README.rst') as file:
    readme = file.read()

setup(name='style',
      packages=['style'],
      version=__version__,
      author='lmittmann',
      description='🌈 Terminal string styling',
      long_description=readme,
      keywords=['style', 'color', 'ansi', 'terminal styling', 'chalk'],
      url='https://github.com/lmittmann/style',
      license='MIT')
