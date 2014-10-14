.. _thumbor.org: http://www.thumbor.org
.. _bower: http://www.bower.io
.. _sphinx: http://www.sphinx-doc.org
.. _compass: http://www.compass-style.org
.. _sass: http://www.sass-lang.com
.. _wyrm: http://www.github.com/snide/wyrm/
.. _grunt: http://www.gruntjs.com
.. _node: http://www.nodejs.com
.. _demo: http://docs.thumbor.org
.. _hidden: http://sphinx-doc.org/markup/toctree.html

**************************
Thumbor Sphinx Theme
**************************

This is a mobile-friendly sphinx_ theme I made for thumbor.org_. It's
currently in development there and includes some rtd variable checks that can be ignored
if you're just trying to use it on your project outside of that site.

**This repo also exists as a submodule within the thumbor itself**, so please make your edits to
the SASS files here, rather than the .css files on RTD.

.. image:: screen_mobile.png
    :width: 100%
Installation
============

Via package
-----------

Download the package or add it to your ``requirements.txt`` file:

.. code:: bash

    $ pip install thumbor_sphinx_theme

In your ``conf.py`` file:

.. code:: python

    import thumbor_sphinx_theme

    html_theme = "thumbor_sphinx_theme"

    html_theme_path = [thumbor_sphinx_theme.get_html_theme_path()]

Via git or download
-------------------

Symlink or subtree the ``thumbor_sphinx_theme/thumbor_sphinx_theme`` repository into your documentation at
``docs/_themes/thumbor_sphinx_theme`` then add the following two settings to your Sphinx
conf.py file:

.. code:: python

    html_theme = "thumbor_sphinx_theme"
    html_theme_path = ["_themes", ]

How the Table of Contents builds
================================

Currently the left menu will build based upon any ``toctree(s)`` defined in your index.rst file.
It outputs 2 levels of depth, which should give your visitors a high level of access to your
docs. If no toctrees are set the theme reverts to sphinx's usual local toctree.

It's important to note that if you don't follow the same styling for your rST headers across
your documents, the toctree will misbuild, and the resulting menu might not show the correct
depth when it renders.

Also note that the table of contents is set with ``includehidden=true``. This allows you
to set a hidden toc in your index file with the hidden_ property that will allow you
to build a toc without it rendering in your index.

By default, the navigation will "stick" to the screen as you scroll. However if your toc
is vertically too large, it revert to static positioning. To disable the sticky nav
alltogether change the setting in ``conf.py``.

Contributing or modifying the theme
===================================

The thumbor_sphinx_theme is primarily a sass_ project that requires a few other sass libraries. I'm
using bower_ to manage these dependencies and sass_ to build the css. The good news is
I have a very nice set of grunt_ operations that will not only load these dependecies, but watch
for changes, rebuild the sphinx demo docs and build a distributable version of the theme.
The bad news is this means you'll need to set up your environment similar to that
of a front-end developer (vs. that of a python developer). That means installing node and ruby.

Set up your environment
-----------------------

1. Install sphinx_ into a virtual environment.

.. code::

    pip install sphinx

2. Install sass

.. code::

    gem install sass

2. Install node, bower and grunt.

.. code::

    // Install node
    brew install node

    // Install bower and grunt
    npm install -g bower grunt-cli

    // Now that everything is installed, let's install the theme dependecies.
    npm install

Now that our environment is set up, make sure you're in your virtual environment, go to
this repository in your terminal and run grunt:

.. code::

    grunt

This default task will do the following **very cool things that make it worth the trouble**.

1. It'll install and update any bower dependencies.
2. It'll run sphinx and build new docs.
3. It'll watch for changes to the sass files and build css from the changes.
4. It'll rebuild the sphinx docs anytime it notices a change to .rst, .html, .js
   or .css files.
