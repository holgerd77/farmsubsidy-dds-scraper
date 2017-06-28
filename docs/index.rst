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

The project has its own `organization on GitHub <https://github.com/openfarmsubsidies>`_ 
and consists of the following repositories:

+---------------------------------------------------------------------------------------+-----------------------------------------+---------------------+--------------------+
| Name (GitHub)                                                                         | Description                             | Status              | Last Status Update |
+=======================================================================================+=========================================+=====================+====================+
| `openfarmsubsidies-scraper <https://github.com/openfarmsubsidies/scraper>`__          | Scraping                                | ``Beta``            | 2017-06-28         |
+---------------------------------------------------------------------------------------+-----------------------------------------+---------------------+--------------------+
| `openfarmsubsidies-elastic <https://github.com/openfarmsubsidies/elastic>`__          | Search Index                            | ``Beta``            | 2017-06-28         |
+---------------------------------------------------------------------------------------+-----------------------------------------+---------------------+--------------------+ 
| `openfarmsubsidies-backend-api <https://github.com/openfarmsubsidies/backend-api>`__  | Backend/API                             | ``Beta``            | 2017-06-28         |
+---------------------------------------------------------------------------------------+-----------------------------------------+---------------------+--------------------+
| `openfarmsubsidies-frontend <https://github.com/openfarmsubsidies/frontend>`__        | Frontend                                | ``Beta``            | 2017-06-28         |
+---------------------------------------------------------------------------------------+-----------------------------------------+---------------------+--------------------+

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

