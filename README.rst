.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: logo.png

==================
plone.example.form
==================

This is a Plone 5.2 test project to experiment with z3c forms. There are two forms in this project.
The first one is the hallo world form. The second one is a pizza order form.
The inspiration for the second one is from a plone tutorial site here: https://docs.plone.org/develop/addons/schema-driven-forms/creating-a-simple-form/creating-a-package.html. It has been adjusted to work on the Plone 5.2 version.

Features
--------

- Hello world form
- Pizza order form


Examples
--------

This add-on can be seen in action at the following sites:
- http://localhost:8080/Plone/@@hello_world_form for the Hello world form
- http://localhost:8080/Plone/@@pizza_order_form for the Pizza order form


Installation
------------

This project is intedend for testint only. To install plone.example.form run the following::

    $ git clone git@github.com:codehutlabs/plone.example.form.git
    $ cd plone.example.form
    $ plonecli build
    $ plonecli serve

or::

    $ git clone git@github.com:codehutlabs/plone.example.form.git
    $ cd plone.example.form
    $ virtualenv -p python3.7 .
    $ ./bin/pip install -r requirements.txt
    $ ./bin/buildout
    $ ./bin/instance fg

and then opening a browser at http://localhost:8080


Contribute
----------

- Issue Tracker: https://github.com/codehutlabs/plone.example.form/issues
- Source Code: https://github.com/codehutlabs/plone.example.form


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
