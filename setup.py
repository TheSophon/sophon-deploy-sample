#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

from sample import __version__

setup(
    name="sample",
    version=__version__,
    url="https://github.com/TheSophon/sophon_deploy_sample",
    license="MIT",
    description="",
    long_description=open("README.md").read(),
    author="The Sophon",
    author_email="",
    packages=find_packages(exclude=["tests"]),
    zip_safe=False,
    install_requires=[
        "Flask >= 0.10.1, < 1.0.0"
    ],
    entry_points={
        "console_scripts": [
            "runsample = sample.app:main"
        ],
    },
)
