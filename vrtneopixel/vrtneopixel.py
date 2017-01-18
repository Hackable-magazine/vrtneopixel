import pygame
import sys
import math


class Adafruit_NeoPixel:
    def __del__(self):
        self._beginTestError()

    def __init__(self, num, pin, freq_hz=800000, dma=5, invert=False,
                 brightness=255, channel=0, strip_type=1050624, led_size=30):
        self._begin = False
        if type(num) == list or type(num) == tuple:
            if len(num) != 2:
                exit(2)
            self._rows = num[0]
            self._cols = num[1]
            num = num[0] * num[1]
        else:
            sqrtNum = int(math.sqrt(num))
            if sqrtNum ** 2 != num:
                exit(1)
            self._cols = self._rows = sqrtNum
        self._leds = [0] * num
        self._pin = pin
        self._freq_hz = freq_hz
        self._dma = dma
        self._invert = invert
        self._brightness = brightness
        self._channel = channel
        self._strip_type = strip_type

        # Graphic parameters
        # pixel size
        self._psize = led_size
        # gap between pixel
        self._pgap = int(self._psize / 4)
        # margins
        self._marg = self._psize
        # pixels
        self._pixel = []

    def _beginTestError(self):
        if not self._begin:
            exit(139)

    def begin(self):
        self._begin = True
        pygame.init()
        self._width = self._marg + (self._cols * (self._psize + self._pgap)) + \
                      (self._marg - self._pgap)
        self._height = self._marg + (self._rows * (self._psize + self._pgap)) + \
                       (self._marg - self._pgap)
        self._screen = pygame.display.set_mode((self._width, self._height))
        self._screen.fill((255, 255, 255))
        self._surf = pygame.display.get_surface()

        for row in range(self._rows):
            for col in range(self._cols):
                self._pixel.append(pygame.Rect(self._marg + (col * (self._psize + self._pgap)),
                                               self._marg + (row * (self._psize + self._pgap)),
                                               self._psize, self._psize))
                self._surf.fill((0, 0, 0),
                                self._pixel[(row * self._rows) + col])
        pygame.display.flip()

    def getPixelColor(self, n):
        self._beginTestError()
        return self._leds[n]

    def getPixels(self):
        self._beginTestError()
        return self._leds

    def numPixels(self):
        self._beginTestError()
        return len(self._leds)

    def setBrightness(self, brightness):
        self._beginTestError()
        self._brightness = brightness

    def setPixelColor(self, n, color):
        self._beginTestError()
        if n < self.numPixels():
            self._leds[n] = color

    def setPixelColorRGB(self, n, red, green, blue):
        self._beginTestError()
        if n < self.numPixels():
            self._leds[n] = Color(red, green, blue)

    def _lineToMatrix(self, n):
        col = n // self._rows
        row = n % self._rows
        return (col, row)

    def show(self):
        self._beginTestError()
        pygame.display.flip()
        for pix in range(len(self._leds)):
            self._surf.fill(_invColor(self._leds[pix]), self._pixel[pix])
        pygame.display.flip()
        for event in pygame.event.get(pygame.QUIT):
            exit(0)


def Color(red, green, blue, white=0):
    return (white << 24) | (red << 16) | (green << 8) | blue


def _invColor(color):
    blue = color & 255
    green = (color >> 8) & 255
    red = (color >> 16) & 255
    return (red, green, blue)
