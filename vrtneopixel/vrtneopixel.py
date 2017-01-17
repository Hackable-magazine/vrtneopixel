import sys
import math
import matplotlib.pyplot as plt


class Adafruit_NeoPixel:
    def __del__(self):
        self._beginTestError()

    def __init__(self, num, pin, freq_hz=800000, dma=5, invert=False,
                 brightness=255, channel=0, strip_type=1050624, led_width=45,
                 led_height=30):
        self._begin = False
        if type(num) == list or type(num) == tuple:
            if len(num) != 2:
                exit(2)
            self._cols = num[0]
            self._rows = num[1]
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
        self._led_width = led_width
        self._led_height = led_height
        self._markerSize = 180 // max(self._cols, self._rows)

    def _beginTestError(self):
        if not self._begin:
            exit(139)

    def begin(self):
        self._begin = True
        self._fig = plt.gcf()
        self._fig.canvas.set_window_title('WS2812B Matrix Emulator')

        plt.axis([-1, self._cols, -1, self._rows])
        plt.axis('off')
        plt.ion()
        for row in range(self._rows):
            for col in range(self._cols):
                plt.plot(col, row, marker='s', markersize=self._markerSize,
                         color='black')
        plt.show()

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
        plt.clf()
        plt.axis([-1, self._cols, -1, self._rows])
        plt.axis('off')
        for pixel in range(len(self._leds)):
            col, row = self._lineToMatrix(pixel)
            plt.plot(col, row, marker='s', markersize=self._markerSize,
                     color=_invColor(self._leds[pixel]))
        plt.pause(0.0001)


def Color(red, green, blue, white=0):
    return (white << 24) | (red << 16) | (green << 8) | blue


def _invColor(color):
    blue = color & 255
    green = (color >> 8) & 255
    red = (color >> 16) & 255
    return (red / 255, green / 255, blue / 255)
