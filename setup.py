#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['pandas', 'argparse',]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', 'requests']

setup(
    author="Isabelle Berger",
    author_email='isabelle@gwu.edu',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="drosSRA builds a url for visualization of tracks based on user specified parameters (i.e. sex, tissue, cell type)",
    entry_points={
        'console_scripts': [
            'drosSRA=drosSRA.drosSRA:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='drosSRA',
    name='drosSRA',
    packages=find_packages(include=['drosSRA']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/isabelleberger/drosSRA',
    version='0.4.0',
    zip_safe=False,
)
