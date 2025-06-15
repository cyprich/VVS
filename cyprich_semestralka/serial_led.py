import time
from machine import Pin
from neopixel import NeoPixel

from cyprich_semestralka.globals import Globals


class SerialLED:
    def __init__(self):
        self._np: NeoPixel = NeoPixel(Pin(8), 3)
        self._delay = 0.15

        self._brightness: int = 255
        self.update_brightness()

    def success(self, i: int):
        self.turn_off()
        self._np[i] = (0, self._brightness, 0)
        self._np.write()

    def fail(self):
        self.turn_off(True)
        self._np.fill((self._brightness, 0, 0))
        self._np.write()

    def turn_off(self, write: bool = False):
        self._np.fill((0, 0, 0))
        self._np.write() if write else None

    def deinit(self):
        self.turn_off(True)
        pass

    def update_brightness(self):
        self._brightness: int = int(Globals.brightness * 255)
