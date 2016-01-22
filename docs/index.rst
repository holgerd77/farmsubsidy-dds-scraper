.. farmsubsidy-dds documentation master file, created by
   sphinx-quickstart on Wed Jan 20 09:32:01 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

farmsubsidy-dds - EU Farmsubsidy Scrapers
=========================================

This is the project documentation for ``farmsubsidy-dds``, a new approach on 
building an open scraper infrastructure and user interface for 
researching EU farmsubsidy payments, build upon the experiences made during
work on historically grown Farmsubsidy.org 
`tech infrastructure <http://farmsubsidy.readthedocs.org>`_.

The project consists of the following sub components:

+-----------------------------+-----------------------------------------+---------------------+---------------------------------------------------------------------------------------------+
| Name                        | Description                             | Status              | Last Status Update | Repository                                                             |
+=============================+=========================================+=====================+=============================================================================================+
| farmsubsidy-dds-scraper     | Scraping infrastructure                 | ``Pre-Alpha``       | 2016-01-21         | `GitHub <https://github.com/holgerd77/farmsubsidy-dds-scraper>`__      |
+-----------------------------+-----------------------------------------+---------------------+---------------------------------------------------------------------------------------------+
| farmsubsidy-dds-elastic     | Search Index                            | ``Pre-Alpha``       | 2016-01-22         | `GitHub <https://github.com/holgerd77/farmsubsidy-dds-elastic>`__      |
+-----------------------------+-----------------------------------------+---------------------+---------------------------------------------------------------------------------------------+ 
| farmsubsidy-dds-backend-api | Backend/API                             | ``Not Started``     | 2016-01-21         | `GitHub <https://github.com/holgerd77/farmsubsidy-dds-backend-api>`__  |
+-----------------------------+-----------------------------------------+---------------------+---------------------------------------------------------------------------------------------+
| farmsubsidy-dds-frontend    | Frontend                                | ``Not Started``     | 2016-01-21         | `GitHub <https://github.com/holgerd77/farmsubsidy-dds-frontend>`__     |
+-----------------------------+-----------------------------------------+---------------------+---------------------------------------------------------------------------------------------+

This documentation provides guidance for installation, setup and technical
aspects for the different sub modules.

Contents:

.. toctree::
   :maxdepth: 2
   
   scraping.rst
   elastic.rst
   backend_api.rst
   frontend.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

