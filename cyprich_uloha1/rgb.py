"""First part/option of the assignment.

Turns on one of seven basic RGB colors based on user choice
"""

from machine import Pin
from cyprich_uloha1.color import Color
from cyprich_uloha1.utils import decider


class RGB:
    """Class that controls turning on and off one of seven basic RGB colors."""

    def __init__(self):
        """Create instance of the class."""
        self._r: Pin = Pin(21, Pin.OUT)
        self._g: Pin = Pin(11, Pin.OUT)
        self._b: Pin = Pin(10, Pin.OUT)

        self._colors: list[Color] = []
        self._colors.append(Color(True, False, False, "Red"))
        self._colors.append(Color(False, True, False, "Green"))
        self._colors.append(Color(False, False, True, "Blue"))
        self._colors.append(Color(True, True, False, "Yellow"))
        self._colors.append(Color(True, False, True, "Magenta"))
        self._colors.append(Color(False, True, True, "Cyan"))
        self._colors.append(Color(True, True, True, "White"))

    def run(self):
        """Turn on one of seven basic RGB colors.

        User is being asked which color to turn on. The color turns on
        when <Enter> is pressed.
        """
        print("\n--- RGB ---")
        user: int = decider("Choose one from colors to show",
                            *[i.name for i in self._colors]) - 1

        self._r.value(self._colors[user].r)
        self._g.value(self._colors[user].g)
        self._b.value(self._colors[user].b)

        input("Press enter to stop...")
        self.stop()

    def stop(self):
        """Turn off all colors."""
        self._r.off()
        self._g.off()
        self._b.off()
