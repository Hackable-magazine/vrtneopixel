from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vrtneopixel',

    packages=['vrtneopixel'],

    version='1.0.10',

    description='A WS2812 matrix emulator',
    long_description=long_description,

    url='https://github.com/Hackable-Magazine/vrtneopixel',

    author='Tristan Colombo',
    author_email='tristan.colombo@gmail.com',

    license='GPLv3+',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: System :: Emulators',

        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Programming Language :: Python :: 3',
    ],

    keywords='emulator ws2812 neopixel rpi_ws281x RaspberryPi',

    install_requires=['matplotlib'],
)
