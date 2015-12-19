#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("requirements.txt") as f:
    requirements = [req.strip() for req in f.readlines()]

test_requirements = [
    "nose",
    "coverage",
    "mock",
    "coveralls",
    "flake8"
]

os.chdir("propiedades")

setup(
    name='propiedades',
    version='0.0.1',
    description="Python django project to scrape properties prices.",
    url='https://github.com/chadad/propiedades',
    download_url='https://github.com/chadad/propiedades/archive/master.zip',
    packages=[
        'propiedades',
        'scraper',
        'webapp'
    ],
    package_dir={'propiedades': 'propiedades'},
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3+",
    zip_safe=False,
    keywords="properties prices scraping",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Office/Business'
    ],
    test_suite='nose.collector',
    tests_require=test_requirements
)
