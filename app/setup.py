#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from setuptools import setup, find_packages
import platform
import sys

# Main dependences
# Custom dependences
deps = ['requests', 'cleverbot', 'pytube', 'moviepy', 'wolframalpha', 'prettytable', 'trueskill']

if sys.version_info < (2,7):
    deps += ['importlib']

if platform.system().lower() == "windows":
    deps.append('pyreadline')
else:
    try:
        import readline
    except ImportError:
        deps.append('readline')

setup(
    name='otaku bot',
    version=1,
    url='http://github.com/cristopher29/WaBot',
    license='GPL-3+',
    author='cristopher29',
    tests_require=[],
    install_requires = deps,
    #cmdclass={'test': PyTest},
    author_email='',
    description='A Otaku WhatsApp bot',
    #long_description=long_description,
    packages= find_packages(),
    include_package_data=True,
    platforms='any',
    #test_suite='',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 1 - Alpha',
        'Natural Language :: English - Spanish',
        #'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
    #extras_require={
    #    'testing': ['pytest'],
    #}
)
