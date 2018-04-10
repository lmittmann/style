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
      license='MIT',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'])
