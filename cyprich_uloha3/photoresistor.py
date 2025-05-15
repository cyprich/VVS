"""Manages the photoresistor.

You can read the value from photoresistor in two ways:
- Absolute value: returns integer, as value from photoresistor in u16 units
- Relative value (percent): returns float, as the percentage of light,
    where 100% is full bright and 0% is full dark
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
