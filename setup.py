# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='homebridge-pi-lamp',
    version='0.1',
    description='An integration of the Raspberry Pi, the Unicorn pHAT and Homebridge.',
    url='https://github.com/mkoistinen/homebridge-pi-lamp',
    author='Martin Koistinen',
    author_email='mkoistinen@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'django>2.2,<2.3',
        'unicornhat>=2.2.3',
    ]
)
