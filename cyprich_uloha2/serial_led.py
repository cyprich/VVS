"""First part/option of the assignment.

Allows user to choose the number of serial LEDs Allows user to specify
color of these LEDs
"""
import neopixel
from machine import Pin
from cyprich_uloha2.utils import inputer, rgb_inputer


class SerialLed:
    """Controls serial LEDs and their color."""

    def __init__(self, led_number: int = 3) -> None:
        """Create instance of the class."""
        self._pin_number = 8
        self._count = led_number
        self._np = neopixel.NeoPixel(Pin(self._pin_number), self._count)

    def set_single(self, led_number: int, value: tuple[int, int, int]) -> None:
        """Set color to single LED from all serial LEDs."""
        self._np[led_number] = value
        self._np.write()

    def set(self, count, value: tuple[int, int, int]) -> None:
        """Set color to specified amount of LEDs.

        Uses 'set_single' method
        """
        for i in range(count):
            self.set_single(i, value)


def main() -> None:
    """Run the first part of the assignment."""
    count = inputer("How many leds you want to change?", 1, 4)
    values = rgb_inputer("Enter color values for LEDs")

    np = SerialLed(count)
    np.set(count, values)


if __name__ == '__main__':
    main()
