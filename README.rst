WS2812 Matrix Emulator
=======================

This module can be used to emulate a WS2812 Matrix in replacement of the
``neopixel.py`` module for the Raspberry Pi provided by the **rpi_ws281x** project 
(<https://github.com/jgarff/rpi_ws281x>).

You must only change one line of your code in order to switch between 
emulator and real matrix. Replace the line

  from neopixel import *
by

  from vrtneopixel import *
The number of leds of your matrix is specified in the ``Adafruit_NeoPixel()``
call as the first parameter. We generally use a ``LED_COUNT`` variable and two 
types are allowed:

* simple integer : total number of leds in the matrix, must have an integer square root (ie. 16 -> 4x4 matrix, etc.).

* tuple (rows, cols) : number of rows and columns of the matrix.

----

Émulateur d'écran WS2812
=========================

Ce module peut être utilisé pour émuler un écran de leds WS2812 Matrix en 
remplacement du module ``neopixel.py`` pour Raspberry Pi fourni par le projet 
**rpi_ws281x** (<https://github.com/jgarff/rpi_ws281x>).

Vous devez seulement changer une ligne de votre code pour basculer entre
l'émulateur et l'écran de leds. Remplacez la ligne

  from neopixel import *
par

  from vrtneopixel import *
Le nombre de leds de l'écran est passé en tant que premier paramètre lors de
l'appel à ``Adafruit_NeoPixel()``. On utilise en général une variable ``LED_COUNT`` 
pour laquelle deux types sont autorisés:

* un entier simple : nombre total de leds composant l'écran, doit avoir une racine carrée entière (ie. 16 -> 4x4 matrix, etc.).

* un tuple (rows, cols) : nombre de lignes et de colonnes de l'écran.
