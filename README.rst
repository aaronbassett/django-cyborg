=============================
django-cyborg
=============================

.. image:: https://badge.fury.io/py/django-cyborg.png
    :target: https://badge.fury.io/py/django-cyborg
    :alt: Current PyPi version

.. image:: https://travis-ci.org/aaronbassett/django-cyborg.png?branch=master
    :target: https://travis-ci.org/aaronbassett/django-cyborg
    :alt: Build status

.. image:: https://requires.io/github/aaronbassett/django-cyborg/requirements.svg?branch=master
     :target: https://requires.io/github/aaronbassett/django-cyborg/requirements/?branch=master
     :alt: Requirements Status

A simple way to add robots.txt and humans.txt to your Django project

Quickstart
----------

Install django-cyborg::

    pip install django-cyborg

Add cyborg your INSTALLED_APPS::

    INSTALLED_APPS=[
        ...
        'cyborg',
    ]

Add cyborg to your urls.py::

    url(r'^', include('cyborg.urls')),

Customising
-----------

To add your own text to either `robots.txt` or `humans.txt` simply override
the relevant template. Create a `cyborg/robots.txt` or a `cyborg/humans.txt`
and place it somewhere that is discoverable by your template loader.

Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements/test.txt
    (myenv) $ python runtests.py

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-pypackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-pypackage`: https://github.com/pydanny/cookiecutter-djangopackage
