"""First part/option of the assignment.

Allows user to choose the number of serial LEDs Allows user to specify
color of these LEDs
"""
import neopixel
from machine import Pin


class SerialLED:
    """Controls serial LEDs and their color."""

    def __init__(self) -> None:
        """Create instance of the class."""
        self._pin_number = 8
        self._np = neopixel.NeoPixel(Pin(self._pin_number), 3)
        self._max_value = 255

    def set(self, led_number: int, r_percent: float, g_percent: float, b_percent: float) -> None:
        """Set color to specified LED from all serial LEDs."""
        values = [int(i * self._max_value) for i in [r_percent, g_percent, b_percent]]
        self._np[led_number] = values
        self._np.write()
