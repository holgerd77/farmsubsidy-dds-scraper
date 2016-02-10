==========================
Backend/API (Python/Flask)
==========================

Backend/API for creating a simple API layer and connecting to ``Elastic``.

Installation
============

Installation is done by cloning the repository and install the dependencies
from the requirements files::

    pip install -r requirements.txt
    pip install -r requirements_dev.txt # DEV requirements

The project uses ``Python 3.5`` and is build upon the following main 
``Python/Flask`` libraries:

* `Flask 0.10 <http://flask.pocoo.org/>`_

The dev server on ``http://127.0.0.1:5000`` can be started with::

    python app.py

API
===

General
-------

Current version of the API: ``v1``

Common Request Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------------+------------------------------------------------------+-------------------------------+
| Name               | Description                                          | Example Values                |
+====================+======================================================+===============================+
| start              | Result object to start with (default: 0)             | 0, 9 (10th object!            |
+--------------------+------------------------------------------------------+-------------------------------+
| rows               | Number of rows/objects to return (default: 10)       | 1, 10, 25                     |
+--------------------+------------------------------------------------------+-------------------------------+


Common Behaviour
^^^^^^^^^^^^^^^^

API always returns ``aggregations`` for ``towns``, ``years``, ``countries`` and ``sub payments type``.

Payments Endpoint
-----------------

``Payments`` endpoint can be reached at::

    /[API_VERSION]/payments/

Results are sorted by ``amount_euro`` by default.

Endpoint-specific Request Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+--------------------+------------------------------------------------------+-------------------------------+
| Name               | Description                                          | Example Values                |
+====================+======================================================+===============================+
| q                  | Generic search for recipient, town or ZIP code       | Nestle,London,NR16            |
+--------------------+------------------------------------------------------+-------------------------------+
| name               | Recipient name                                       | Nestle                        |
+--------------------+------------------------------------------------------+-------------------------------+
| country            | 2-letter country code of an EU country               | GB,SI,NL,PL                   |
+--------------------+------------------------------------------------------+-------------------------------+
| zip_code           | ZIP code of a European town                          | NR16                          |
+--------------------+------------------------------------------------------+-------------------------------+
| town               | Name of a European town or city                      | London                        |
+--------------------+------------------------------------------------------+-------------------------------+
| year               | Year of payment                                      | 2014                          |
+--------------------+------------------------------------------------------+-------------------------------+
| country            | 2-letter country code of an EU country               | GB,SI,NL,PL                   |
+--------------------+------------------------------------------------------+-------------------------------+
| amount_euro_gte    | Amount euro greater than given value                 | 2500,100000,1000000           |
+--------------------+------------------------------------------------------+-------------------------------+
| sub_payments_type  | Type of the sub payment in national language         | Direct Aid                    |
+--------------------+------------------------------------------------------+-------------------------------+

Example Requests
^^^^^^^^^^^^^^^^

::

  https://[URL_TO_API]/[API_VERSION]/payments/?amount_euro_gte=5000&town=London

Example Data Set
^^^^^^^^^^^^^^^^

::

  _source: {
    town: "London",
    nc_symbol: "GBP",
    amount_nc: 6568,
    name: "Example Recipient",
    amount_euro: 8631.32,
    country: "GB",
    sub_payments_euro: [
      {
        amount: 8630.66,
        name: "Rural Development"
      },
      {
        amount: 0,
        name: "Direct Aid"
      },
      {
        amount: 0,
        name: "Market Schemes"
      }
    ],
    sub_payments_nc: [
      {
        amount: 6567.5,
        name: "Rural Development"
      },
      {
        amount: 0,
        name: "Direct Aid"
      },
      {
        amount: 0,
        name: "Market Schemes"
      }
    ],
    year: 2014,
    nc_conv_rate: 0.76095,
    nc_conv_date: "2016-01-26",
    zip_code: "SW7"
  }

``Sub payments`` are indexed schemaless as they are provided by the specific country
agencies.

.. note::
   If both an ``amount_nc`` (national currency) and an ``amount_euro`` is provided,
   the Euro value is not coming originally from the source but is calculated via
   ``fixer.io`` API with the given conv rate at the conv date provided.

Countries Endpoint
------------------

TODO










