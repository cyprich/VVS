from machine import PWM

from cyprich_semestralka.globals import Globals
from cyprich_semestralka.entry import Entry


class Buzzer:
    def __init__(self):
        self._buz = PWM(5)
        self._buz.duty_u16(0)

        self._SUCCESS_FREQ: tuple[int, int, int] = (220, 330, 440)
        self._FAIL_FREQ: int = 220

    def play(self, entry: Entry) -> None:
        self._set_volume()
        _, freq, _ = entry  # extract frequency from entry
        self._buz.freq(freq)

    def turn_off(self):
        self._buz.duty_u16(0)

    def _set_volume(self):
        self._buz.duty_u16(int(Globals.MAX_VOLUME_PWM * Globals.volume))

    def success(self, i: int):
        self._set_volume()
        self._buz.freq(self._SUCCESS_FREQ[i])

    def fail(self):
        self._set_volume()
        self._buz.freq(self._FAIL_FREQ)

    def deinit(self):
        self._buz.deinit()