"""Third part/option of the assignment.

Plays one of five melodies, based on user choice. Volume can be changed
with button press. Uses external library "Music".
"""

import time
from machine import Pin

from cyprich_uloha1.play import playsong, set_volume, melody
from cyprich_uloha1.utils import decider


class Melody:
    """Class that controls the melody."""

    def __init__(self):
        """Create instance of the class."""
        self._max_volume: int = 1000
        self._volume: int = self._max_volume // 2

        self._available_melodies: list[str] = [
            "Star Trek Intro",
            "Silent Night",
            "Pacman",
            "Ode an die Freude",
            "Star Wars theme"]
        self._index: int = 0

        self._button: Pin = Pin(2, Pin.IN, Pin.PULL_UP)
        self._button.irq(
            handler=lambda x: self.change_volume(),
            trigger=Pin.IRQ_RISING)

        self._delay: float = 0.15
        self._time_before: int = 0

    def run(self):
        """Start the melody."""
        set_volume(self._volume)

        self._index: int = decider(
            "Choose which song you want to play",
            *self._available_melodies)
        playsong(melody[self._index - 1])

    def change_volume(self):
        """Change volume of the buzzer."""
        if time.time() - self._time_before > self._delay:
            self._time_before = time.time()

            self._volume += self._max_volume // 4

            if self._volume > self._max_volume:
                self._volume = 0

            set_volume(self._volume)
            print(f"[Volume: {self._volume // 10}%]")
