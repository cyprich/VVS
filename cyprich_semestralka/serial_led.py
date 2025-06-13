import time
from machine import Pin
from neopixel import NeoPixel

from cyprich_semestralka.globals import Globals


class SerialLED:
    def __init__(self):
        self._np: NeoPixel = NeoPixel(Pin(8), 3)
        self._delay = 0.15

        self._brightness: int
        self.update_brightness()

    def success(self):
        for i in range(3):
            self.shut_off()
            self._np[i] = (0, self._brightness, 0)
            self._np.write()

            self._sleep()

        self.shut_off(True)

    def fail(self):
        for i in range(3):
            self.shut_off(True)
            self._sleep()

            self._np.fill((self._brightness, 0, 0))
            self._np.write()
            self._sleep()

        self.shut_off(True)

    def _sleep(self):
        # TODO
        time.sleep(self._delay)

    def shut_off(self, write: bool = False):
        self._np.fill((0, 0, 0))
        self._np.write() if write else None

    def deinit(self):
        self.shut_off(True)
        pass

    def update_brightness(self):
        self._brightness: int = int(Globals.brightness * 255)
