import time

from du1.play import *
from du1.utils import decider


class Melody:
    def __init__(self):
        self._max_volume = 1000
        self._volume = self._max_volume // 2

        self._available_melodies = ["Star Trek Intro", "Silent Night", "Pacman", "Ode an die Freude", "Star Wars theme"]
        self._index = decider("Choose which song you want to play", *self._available_melodies)

        self._button = Pin(2, Pin.IN, Pin.PULL_UP)
        self._button.irq(handler=lambda x: self.change_volume(), trigger=Pin.IRQ_RISING)

        self._delay = 0.15
        self._time_before = 0


    def run(self):
        set_volume(self._volume)
        playsong(melody[self._index - 1])


    def change_volume(self):
        if time.time() - self._time_before > self._delay:
            self._time_before = time.time()

            self._volume += int(self._max_volume / 4)

            if self._volume > self._max_volume:
                self._volume = 0

            set_volume(self._volume)
            print(f"[Volume: {self._volume // 10}%]")



