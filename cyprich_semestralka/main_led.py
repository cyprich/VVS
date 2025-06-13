from machine import PWM

from cyprich_semestralka.globals import Globals
from cyprich_semestralka.entry import Entry


class MainLED:
    def __init__(self):
        self._r: PWM = PWM(21, freq=120, duty_u16=0)
        self._g: PWM = PWM(11, freq=120, duty_u16=0)
        self._b: PWM = PWM(10, freq=120, duty_u16=0)

    def set(self, entry: Entry):
        color, _, _ = entry  # extract the color from entry

        for i in color:
            if i < 0 or i > 255:
                return

        # scales color from rgb (0-255) to duty_u16 (0-MAX_PWM) and adds brightness
        scale_coef: float = Globals.MAX_PWM / 255 * Globals.brightness

        self._r.duty_u16(int(color[0] * scale_coef))
        self._g.duty_u16(int(color[1] * scale_coef))
        self._b.duty_u16(int(color[2] * scale_coef))

    def turn_off(self):
        self._r.duty_u16(0)
        self._g.duty_u16(0)
        self._b.duty_u16(0)

    def deinit(self):
        self._r.deinit()
        self._g.deinit()
        self._b.deinit()
