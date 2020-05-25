==============
DRF Generators
==============

Generate all of your Views, Serializers, and even Urls for your Django Rest Framework application with one command!

This is **ONLY** to jumpstart your development and save you from writing the same code over and over for each model. Please go through complete code and validate.

---------------

|python| |pypi| |license| |travis| |django| |drf|

---------------

* `Installation`_
* `Usage`_
* `Tests`_
* `License`_

---------------

============
Installation
============

.. code-block:: bash

    $ git clone https://github.com/vickybiswas/drf-generators.git
    $ cd drf-generators
    $ python setup.py install

To use DRF Generators, add it your INSTALLED_APPS.

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'rest_framework',
        'drf_generators',
        ...
    )

*Note*: In order to use the APIView classes, you must have the rest framework DEFAULT_PAGINATION_CLASS and PAGE_SIZE set.

.. code-block:: python

    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 15
    }

-----------------

=====
Usage
=====

To use the generators, run the following command, where ``app`` is the application to generate an API for.

.. code-block:: bash

   $ python manage.py generate {app} {options}

========================== ===================================================
Option                     Action
========================== ===================================================
``--serializers``          Generate only Serializers for your app.
``--views``                Generate only Views for your app.
``--urls``                 Generate only urls for your app.
``--force``                Overwrite existing files without the warning prompt.
``-f``, ``--format``       Format to use when generating views and urls. Valid options: ``viewset``, ``apiview``, ``function``, ``modelviewset``. Default: ``viewset``.
``-d``, ``--depth``        Serialization depth for related models. Default: 0
========================== ===================================================

**Example:** Generate everything for the app ``api`` with function style views, overwriting existing files, with a serialization depth of 2.

.. code-block:: bash

    $ python manage.py generate api --format function --force -- depth=2

-------------------

=====
Tests
=====

A full application built with drf-generators can be found in the `tests directory <http://github.com/vickybiswas/drf-generators/tree/master/tests>`_. Instructions on running the tests can be found in the test project's README.


=======
License
=======

MIT License. See `LICENSE <https://github.com/brobin/drf-generators/blob/master/LICENSE>`_.

This was cloned and made fit to our purpose from https://github.com/Brobin/drf-generators. 

.. |python| image:: https://img.shields.io/pypi/v/drf-generators.svg?style=flat-square
    :target: https://pypi.python.org/pypi/drf-generators/
    :alt: Supported Python versions

.. |pypi| image:: https://img.shields.io/pypi/pyversions/drf-generators.svg?style=flat-square
    :target: https://pypi.python.org/pypi/drf-generators/
    :alt: Latest Version

.. |license| image:: https://img.shields.io/pypi/l/drf-generators.svg?style=flat-square
    :target: https://pypi.python.org/pypi/drf-generators/
    :alt: License

.. |travis| image:: https://img.shields.io/travis/Brobin/drf-generators.svg?style=flat-square
    :target: https://travis-ci.org/Brobin/drf-generators/
    :alt: Travis CI

.. |django| image:: https://img.shields.io/badge/Django-1.11, 2.2,3.0-orange.svg?style=flat-square
    :target: http://djangoproject.com/
    :alt: Django 1.11, 2.2, 3.0

.. |drf| image:: https://img.shields.io/badge/DRF-3.11-orange.svg?style=flat-square
    :target: http://www.django-rest-framework.org/
    :alt: DRF 3.11
