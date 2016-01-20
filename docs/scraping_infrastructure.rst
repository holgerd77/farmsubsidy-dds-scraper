====================================
Scraping Infrastructure (Django/DDS)
====================================

Introduction
------------

The scraping infrastructure is build on ``Python/Django`` and is using the
`djang-dynamic-scraper <https://github.com/holgerd77/django-dynamic-scraper>`_
scraping library at its core.

Scrapers for the various EU member state agencies databases are build and maintained
within the Django admin interface.

.. image:: imgs/screenshot_django-admin_scraper_list.png


Installation
------------

The scraping infrastructure project can be installed by cloning the 
`GitHub <https://github.com/holgerd77/farmsubsidy-dds>`__ repository and 
install the requirements into a ``Python 2.7`` virtualenv (switch to 
``Python 3`` planned some time after ``Scrapy/Twisted`` is ported) with::

    pip install -r requirements.txt
    pip install -r requirements_dev.txt # DEV requirements

The project uses the following main ``Python/Django`` libraries:

* `Django 1.8 <https://www.djangoproject.com/>`_
* `Scrapy 0.24 <http://scrapy.org/>`_
* `Django Dynamic Scraper 0.9 <django-dynamic-scraper.readthedocs.org/en/latest/>`_

Configuration
-------------

The following environment variables have to be found in your shell environment,
e.g. by adding lines like ``export FARMSUBSIDY_DDS_SECRET_KEY="..."`` to the
``.bash_profile`` file:

+-------------------------------+---------------------------------------------+--------------------+
| Key                           | Description                                 | Place              |
+===============================+=============================================+====================+
|``FARMSUBSIDY_DDS_SECRET_KEY`` | Project specific Django secret key          | ``settings.py``    |
+-------------------------------+---------------------------------------------+--------------------+

Starting a local Django server should now provide access to the scraper management
admin console via the browser (go to ``127.0.0.1:8000``)::

    python manage.py runserver


Importing/exporting Scrapers
----------------------------

Scrapers can be found in the ``scraper_dumps`` directory inside the repository and imported
with the following command::

    python manage.py loaddata scraper_dumps/farmsubsidy_scraper_dump_YYYY-MM-DD_dds_[DDS_VERSION_NUMBER].json #Generic
    python manage.py loaddata scraper_dumps/farmsubsidy_scraper_dump_2016-01-18_dds_v094.json #Example

.. note::
   It is recommended to match the project installation DDS version with the version from the scraper
   dump, otherwise DB changes during DDS version changes have to be looked at closely in the
   `DDS release notes <http://django-dynamic-scraper.readthedocs.org/en/latest/development.html#releasenotes>`_
   and manual adoptions to the JSON dump format might be necessary.


Creating a new Scraper
----------------------

TODO

Running a Scraper
-----------------

Scraper can be run from the command line with the following command::

    scrapy crawl --output=test.json --output-format=jsonlines payment_spider -L DEBUG -a id=GB -a max_items_read=4 -a max_pages_read=2

This will run the scraper connected to the ``Agency`` in the Django admin with the id ``GB`` and
write the output in a ``JSON Lines`` formatted file called ``test.json``.

Usage options for scraping behaviour can be found in the corresponding  DDS doc section for
`running/testing scrapers <http://django-dynamic-scraper.readthedocs.org/en/latest/getting_started.html#running-testing-your-scraper>`_.


JSON Data Format
----------------

TODO
