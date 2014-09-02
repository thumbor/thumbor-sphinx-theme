# -*- coding: utf-8 -*-
"""`thumbor_sphinx_theme` lives on `Github`_.

.. _github: https://www.github.com/thumbor/thumbor_sphinx_theme

"""
from setuptools import setup
from thumbor_sphinx_theme import __version__


setup(
    name='thumbor_sphinx_theme',
    version=__version__,
    url='https://github.com/thumbor/thumbor_sphinx_theme/',
    license='MIT',
    author='Ricardo Dani',
    author_email='ricardo.dani@corp.globo.com',
    description='Thumbor theme for Sphinx, 2014 version.',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=['thumbor_sphinx_theme'],
    package_data={'thumbor_sphinx_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/font/*.*'
    ]},
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
