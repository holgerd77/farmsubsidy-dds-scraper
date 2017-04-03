.. openfarmsubsidies documentation master file, created by
   sphinx-quickstart on Wed Jan 20 09:32:01 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

OpenFarmsubsidies - EU Farmsubsidy Scrapers
===========================================

This is the project documentation for ``openfarmsubsidies``, a new approach on 
building an open scraper infrastructure and user interface for 
researching EU farmsubsidy payments, build upon the experiences made during
work on historically grown Farmsubsidy.org 
`tech infrastructure <http://farmsubsidy.readthedocs.org>`_.

The project consists of the following sub components:

+-------------------------------------------------------------------------------------------------+-----------------------------------------+---------------------+--------------------+
| Name (GitHub)                                                                                   | Description                             | Status              | Last Status Update |
+=================================================================================================+=========================================+=====================+====================+
| `openfarmsubsidies-scraper <https://github.com/holgerd77/openfarmsubsidies-scraper>`__          | Scraping                                | ``Alpha``           | 2016-02-05         |
+-------------------------------------------------------------------------------------------------+-----------------------------------------+---------------------+--------------------+
| `openfarmsubsidies-elastic <https://github.com/holgerd77/openfarmsubsidies-elastic>`__          | Search Index                            | ``Alpha``           | 2016-03-04         |
+-------------------------------------------------------------------------------------------------+-----------------------------------------+---------------------+--------------------+ 
| `openfarmsubsidies-backend-api <https://github.com/holgerd77/openfarmsubsidies-backend-api>`__  | Backend/API                             | ``Alpha``           | 2016-03-04         |
+-------------------------------------------------------------------------------------------------+-----------------------------------------+---------------------+--------------------+
| `openfarmsubsidies-frontend <https://github.com/holgerd77/openfarmsubsidies-frontend>`__        | Frontend                                | ``Alpha``           | 2016-03-04         |
+-------------------------------------------------------------------------------------------------+-----------------------------------------+---------------------+--------------------+

This documentation provides guidance for installation, setup and technical
aspects for the different sub modules.

Contents:

.. toctree::
   :maxdepth: 2
   
   scraper.rst
   elastic.rst
   backend_api.rst
   frontend.rst
   deployment.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

