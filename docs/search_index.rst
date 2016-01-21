======================
Search Index (Elastic)
======================

The following version of ``Elastic`` is used for search infrastructure deployment:

* `Elastic 2.1.1 <https://www.elastic.co/>`_



Some internal notes on development
----------------------------------

Awk line appending::

    awk ' {print "{\"index\":{}}\n" $0;}' accounts3.json > accounts4.json


Indexing::

    curl 'localhost:9200/_cat/indices?v'
    curl -XPUT 'localhost:9200/farmsubsidy-dds-test/payment/_bulk?pretty' --data-binary "@test2.jsonlines"
    curl -XDELETE 'localhost:9200/farmsubsidy-dds-test?pretty'


Searching::

    curl 'localhost:9200/farmsubsidy-dds-test/_search?q=PERTH&pretty'