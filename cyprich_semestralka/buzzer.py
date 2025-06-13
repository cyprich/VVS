from machine import PWM

from cyprich_semestralka.globals import Globals
from cyprich_semestralka.entry import Entry


class Buzzer:
    def __init__(self):
        self._buz = PWM(5)
        self._set_volume()

    def play(self, entry: Entry) -> None:
        self._set_volume()
        _, freq, _ = entry  # extract frequency from entry
        self._buz.freq(freq)

    def turn_off(self):
        self._buz.duty_u16(0)

    def _set_volume(self):
        self._buz.duty_u16(int(Globals.MAX_PWM * Globals.volume))

    def deinit(self):
        self._buz.deinit()