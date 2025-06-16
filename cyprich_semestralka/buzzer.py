"""Buzzer.

Class to represent and control buzzer on hardware board. Allows user to
play frequencies based on Entry class. Allows user to play sound of
successful or unsuccessful level.
"""
from machine import PWM

from cyprich_semestralka.globals import Globals
from cyprich_semestralka.entry import Entry


class Buzzer:
    """Buzzer.

    Class to control buzzer.
    """

    def __init__(self):
        """Create instance of the class."""
        self._buz = PWM(5)
        self._buz.duty_u16(0)

        self._success_freq: tuple[int, int, int] = (220, 330, 440)
        self._fail_freq: int = 220

    def play(self, entry: Entry) -> None:
        """Plays frequency based on Entry."""
        self._set_volume()
        _, freq, _ = entry  # extract frequency from entry
        self._buz.freq(freq)

    def turn_off(self) -> None:
        """Stop playing."""
        self._buz.duty_u16(0)

    def _set_volume(self) -> None:
        """Set 'volume' (duty_u16) based on variables in Globals."""
        self._buz.duty_u16(int(Globals.MAX_VOLUME_PWM * Globals.volume))

    def success(self, i: int) -> None:
        """Play sound of successfully completed level."""
        self._set_volume()
        self._buz.freq(self._success_freq[i])

    def fail(self) -> None:
        """Play sound of unsuccessfully completed level."""
        self._set_volume()
        self._set_volume()
        self._buz.freq(self._fail_freq)

    def deinit(self) -> None:
        """Deinitialize the buzzer."""
        self._buz.deinit()
