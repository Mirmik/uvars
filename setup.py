#!/usr/bin/python3

from setuptools import setup
import glob
import os

import uvars

setup(
	name = 'uvars',
	packages = ['uvars'],
	version = uvars.version,
	license='MIT',
	description = 'User variables dictionary for bash, c++, python.',
	author = 'Sorokin Nikolay',
	author_email = 'mirmikns@yandex.ru',
	url = 'https://github.com/mirmik/uvars',
	keywords = ['testing', 'environment'],
	classifiers = [],
	scripts = ["executable/uvars"],
)