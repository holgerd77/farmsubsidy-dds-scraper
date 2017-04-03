======================
Search Index (Elastic)
======================

Searching is done with ``Elastic``, currently the following version is used:

* `Elastic 2.1.1 <https://www.elastic.co/>`_


Installation
------------

Download ``Elastic`` and install in folder ``elasticsearch`` (no version number)
inside the repository.

The local dev server on ``http://localhost:9200`` can then be started with::

    ./server.sh

Index Creation
--------------

Index Template
^^^^^^^^^^^^^^

For indexing template in ``conf/template.json`` is used for mapping and has to be
activated/loaded before first data indexing::
    
    curl -XPUT localhost:9200/_template/template_1 -d '@conf/template.json'

The current mapping for the index can be seen with::

    curl -XGET 'http://localhost:9200/openfarmsubsidies/_mapping/payment?pretty'

Deleting the current template::

    curl -XDELETE localhost:9200/_template/template_1

See installed templates::

    curl -XGET localhost:9200/_template/


Index Management
^^^^^^^^^^^^^^^^
    
List indices::

    curl 'localhost:9200/_cat/indices?v'

Delete index::

    curl -XDELETE 'localhost:9200/openfarmsubsidies?pretty'

Indexing Documents
------------------

Format Pre-Processing
^^^^^^^^^^^^^^^^^^^^^
Input files have to be formatted as ``JSON Lines`` format and are prepared with the
following command for indexing::

    ./jl2elastic inputfile.json

Indexing Documents
^^^^^^^^^^^^^^^^^^

Index data::

    curl -XPUT 'localhost:9200/openfarmsubsidies/payment/_bulk?pretty' --data-binary "@data_elastic.json"

Searching the Index
-------------------

Testing search::

    curl 'localhost:9200/openfarmsubsidies-test/_search?q=PERTH&pretty'

