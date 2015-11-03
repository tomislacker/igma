#!/usr/bin/env python3
from setuptools import setup, find_packages
from codecs import open
from os import path


# Get the long description from the relevant file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='igma',
    version='0.0',

    description='IPTables Git Manager',
    long_description=long_description,

    url='https://github.com/tomislacker/igma',

    author='Ben Tomasik',
    author_email='ben@tomasik.io',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='firewall git iptables',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=[
        'docopt',
        'gitpython',
        'pyaml',
    ],

    extras_require={
        'dev': ['nose', 'pep8'],
        'test': ['coverage'],
    },

    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [
            'igma-check=igma.cli.check:main',
            'igma-dump=igma.cli.dump:main',
            'igma-gen=igma.cli.generate:main'
        ],
    },
)
