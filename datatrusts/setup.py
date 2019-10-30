# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import io
from setuptools import setup, find_packages


# Helpers
def read(*paths):
    """Read a text file."""
    basedir = os.path.dirname(__file__)
    fullpath = os.path.join(basedir, *paths)
    contents = io.open(fullpath, encoding='utf-8').read().strip()
    return contents


# Prepare
PACKAGE = 'datatrusts'
NAME = PACKAGE.replace('_', '-')
INSTALL_REQUIRES = [
    'pandas>=0.22.0',
    'click>=6.7',
    'cchardet>=1.0',
    'jsonschema>=2.5',
    'pypandoc>=1.3.3',
    'gremlinpython',
]
TESTS_REQUIRE = [
    'pylama',
    'tox',
]
README = read('README.md')
VERSION = read(PACKAGE, 'VERSION')
PACKAGES = find_packages(exclude=['examples', 'tests', 'docs'])


# Run
setup(
    name=NAME,
    version=VERSION,
    packages=PACKAGES,
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    extras_require={'develop': TESTS_REQUIRE},
    entry_points={
        'console_scripts': [
            'datatrusts = datatrusts.cli:cli',
        ]
    },
    zip_safe=False,
    long_description=README,
    long_description_content_type='text/markdown',
    description='Create and manage data trusts in Python',
    author='BrightHive',
    author_email='info@brighthive.io',
    url='https://github.com/brighthive/datatrusts',
    license='Apache 2.0',
    keywords=[
        'data trust',
        'open data',
        'data sharing',
    ],
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache 2.0',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)