"""Class to handle the Main LED."""


from machine import PWM

from cyprich_semestralka.globals import Globals
from cyprich_semestralka.entry import Entry


class MainLED:
    """Class to handle the Main LED."""

    def __init__(self):
        """Create instance of the class."""
        self._r: PWM = PWM(21, freq=120, duty_u16=0)
        self._g: PWM = PWM(11, freq=120, duty_u16=0)
        self._b: PWM = PWM(10, freq=120, duty_u16=0)

    def set(self, entry: Entry):
        """Set the color of Main LED based on value from Entry."""
        color, _, _ = entry  # extract the color from entry

        for i in color:
            if i < 0 or i > 255:
                return

        # scales color from rgb (0-255) to duty_u16 (0-MAX_PWM) value
        # also uses brightness
        scale_coef: float = Globals.MAX_VOLUME_PWM / 255 * Globals.brightness

        self._r.duty_u16(int(color[0] * scale_coef))
        self._g.duty_u16(int(color[1] * scale_coef))
        self._b.duty_u16(int(color[2] * scale_coef))

    def turn_off(self):
        """Turn off the Main LED."""
        self._r.duty_u16(0)
        self._g.duty_u16(0)
        self._b.duty_u16(0)

    def deinit(self):
        """Deinitialize the Main LED."""
        self._r.deinit()
        self._g.deinit()
        self._b.deinit()
