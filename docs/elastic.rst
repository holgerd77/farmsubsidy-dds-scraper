======================
Search Index (Elastic)
======================

Searching is done with ``Elastic``, currently the following version is used:

* `Elastic 2.1.1 <https://www.elastic.co/>`_


Installation
------------

Download ``Elastic`` and install in folder ``elasticsearch`` (no version number)
inside the repository.


Index Preparation
-----------------

Input files have to be formatted as ``JSON Lines`` format and are prepared with the
following command for indexing::

    ./jl2elastic inputfile.json


Some internal notes on development
----------------------------------

Indexing::

    curl 'localhost:9200/_cat/indices?v'
    curl -XPUT 'localhost:9200/farmsubsidy-dds-test/payment/_bulk?pretty' --data-binary "@test2.jsonlines"
    curl -XDELETE 'localhost:9200/farmsubsidy-dds-test?pretty'


Searching::

    curl 'localhost:9200/farmsubsidy-dds-test/_search?q=PERTH&pretty'