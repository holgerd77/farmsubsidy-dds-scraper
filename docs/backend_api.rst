==========================
Backend/API (Python/Flask)
==========================

Backend/API for creating a simple API layer and connecting to ``Elastic``.

Installation
------------

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
---

Current version of the API: ``v1``

Payments Endpoint
^^^^^^^^^^^^^^^^^

Payments endpoint can be reached at::

    /[API_VERSION]/payments/


