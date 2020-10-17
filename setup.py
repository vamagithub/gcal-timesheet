# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in gcal_timesheet/__init__.py
from gcal_timesheet import __version__ as version

setup(
	name='gcal_timesheet',
	version=version,
	description='Gcal Timesheet',
	author='Vama',
	author_email='vamagithub@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
