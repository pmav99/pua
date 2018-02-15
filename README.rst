========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/pua/badge/?style=flat
    :target: https://readthedocs.org/projects/pua
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/pmav99/pua.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/pmav99/pua

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/pmav99/pua?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/pmav99/pua

.. |requires| image:: https://requires.io/github/pmav99/pua/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/pmav99/pua/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/pmav99/pua/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/pmav99/pua

.. |version| image:: https://img.shields.io/pypi/v/pua.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pua

.. |commits-since| image:: https://img.shields.io/github/commits-since/pmav99/pua/v0.1.1.svg
    :alt: Commits since latest release
    :target: https://github.com/pmav99/pua/compare/v0.1.1...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/pua.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/pua

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pua.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pua

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pua.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/pua


.. end-badges

A utility providing random user agents.

* Free software: BSD 3-Clause License

Installation
============

::

    pip install pua

Documentation
=============

https://pua.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
