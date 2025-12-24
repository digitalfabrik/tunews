#!/usr/bin/env python3

import os
from setuptools import find_packages, setup

setup(
    name="integreat-tunews",
    version="1.0.0",
    packages=find_packages("src"),
    package_dir={'':'src'},
    include_package_data=True,
    scripts=['src/manage.py'],
    install_requires=[
        "django",
        "django-basicauth",
        "lxml",
        "mysqlclient"
    ],
    author="Tuer an Tuer - Digitalfabrik gGmbH",
    author_email="info@integreat-app.de",
    description="TuNews International Back End for Integreat",
    license="MIT",
    keywords="Django TuNews International",
    url="http://github.com/Integreat/tunews/",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
