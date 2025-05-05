"""Second part/option of the assignment.

Changes the color of RGB LED based on value taken from photoresistor
Uses timers to measure and stop this effect on RGB LED
"""
from machine import Pin, ADC


class Photoresistor:
    """Manages photoresistor."""

    def __init__(self, pin: int = 3) -> None:
        """Create instance of the class."""
        self._photo: ADC = ADC(Pin(pin), atten=ADC.ATTN_11DB)
        self._max_value: int = 65535

    def get_value(self) -> int:
        """Read the value on photoresistor in u16 units."""
        return self._photo.read_u16()

    def get_percent(self) -> float:
        """Read the value on photoresistor in percent."""
        return self.get_value() / self._max_value
