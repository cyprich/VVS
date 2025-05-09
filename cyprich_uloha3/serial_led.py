"""Allows user to control serial LED's with Neopixel."""
import neopixel
from machine import Pin


class SerialLED:
    """Controls serial LEDs and their color."""

    def __init__(self, pin_number: int = 8) -> None:
        """Create instance of the class."""
        self._pin_number = pin_number
        self._np = neopixel.NeoPixel(Pin(self._pin_number), 3)
        self._max_value = 255

    def set(
            self,
            led_number: int,
            r_percent: float,
            g_percent: float,
            b_percent: float) -> None:
        """Set color to specified LED.

        :param: Value for Red, Green and Blue respectively. Expects
            decimal values in range from 0 to 1, where 1 is fully bright
            LED and 0 is fully dark LED.
        """
        values = [int(i * self._max_value)
                  for i in [r_percent, g_percent, b_percent]]
        self._np[led_number] = values
        self._np.write()

    def get_max_value(self) -> int:
        """Return max value."""
        return self._max_value
