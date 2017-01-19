clr
===

|Build Status| |PyPI version|

**clr** is a simple terminal string styling library. Its API is a port of the popular
`chalk <https://github.com/chalk/chalk>`__ module for javascript.


Install
-------

::

    $ pip3 install clr


Usage
-----

.. code:: py

    import clr

    print(clr.red.bold('Hello world!'))


API
---

clr.\ ``<style>[.<style>...](object, [object...])``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chain `styles <#styles>`__ and call the last one as a method with an argument. Order doesn't matter, and later styles
take precedence in case of a conflict, e.g. ``clr.red.yellow.green`` is equivalent to ``clr.green``.

Multiple arguments will be separated by space.


Styles
------

Modifiers
~~~~~~~~~

- ``bold``
- ``bgBold``
- ``dim``
- ``italic``
- ``underline``
- ``inverse``
- ``hidden``
- ``strikethrough``

Colors
~~~~~~

- ``black``
- ``red``
- ``green``
- ``yellow``
- ``blue``
- ``magenta``
- ``cyan``
- ``white``

Background colors
~~~~~~~~~~~~~~~~~

- ``bgBlack``
- ``bgRed``
- ``bgGreen``
- ``bgYellow``
- ``bgBlue``
- ``bgMagenta``
- ``bgCyan``
- ``bgWhite``

.. |Build Status| image:: https://travis-ci.org/lmittmann/clr.svg?branch=master
    :target: https://travis-ci.org/lmittmann/clr
.. |PyPI version| image:: https://img.shields.io/pypi/v/clr.svg
    :target: https://pypi.python.org/pypi/clr
