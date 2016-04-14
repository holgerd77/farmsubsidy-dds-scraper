==============================
Frontend (Boostrap/Javascript)
==============================

Installation
------------

Requirements
^^^^^^^^^^^^

Main runtime library dependencies:

* `Bootstrap 4 <http://v4-alpha.getbootstrap.com/>`_
* `jQuery 2.2 <https://jquery.com/>`_

Main dev tools:

* `Bower <http://bower.io>`_
* `Sass (Ruby installation) <http://sass-lang.com/>`_
* `http-server <https://github.com/indexzero/http-server>`_
* `(Gulp.js) <http://gulpjs.com/>`_ (build automation)

Installation
^^^^^^^^^^^^

Installation ``Bower`` web project dependencies (Bootstrap,...)
from ``bower.json`` with::

  bower install


Running the server
^^^^^^^^^^^^^^^^^^

Run the ``http-server`` from the main folder of the repository::

  http-server

Content is served on ``http://127.0.0.1:8080``, API is expected 
at ``http://127.0.0.1:5000``.

Development
-----------

``Sass`` sources can be compiled with::

  sass sass/content.scss css/content.css
  
Or you can run the ``watch`` command with::

  sass --watch sass/content.scss:css/content.css
