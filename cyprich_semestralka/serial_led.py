"""Class to handle the Serial LED with Neopixel."""

from machine import Pin
from neopixel import NeoPixel

from cyprich_semestralka.globals import Globals


class SerialLED:
    """Class to handle the Serial LED with Neopixel."""

    def __init__(self):
        """Create instance of the class."""
        self._np: NeoPixel = NeoPixel(Pin(8), 3)
        self._delay = 0.15

        self._brightness: int = 255
        self.update_brightness()

    def success(self, i: int):
        """Play animation of successfully passed level."""
        self.turn_off()
        self._np[i] = (0, self._brightness, 0)
        self._np.write()

    def fail(self):
        """Play animation of failed level."""
        self.turn_off(True)
        self._np.fill((self._brightness, 0, 0))
        self._np.write()

    def turn_off(self, write: bool = False):
        """Turn off all LEDs."""
        self._np.fill((0, 0, 0))
        if write:
            self._np.write()

    def deinit(self):
        """Deinitialize the Serial LED."""
        self.turn_off(True)

    def update_brightness(self):
        """Calculate the brightness."""
        self._brightness: int = int(Globals.brightness * 255)
