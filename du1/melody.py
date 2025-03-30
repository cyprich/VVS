from du1.play import *
from du1.utils import decider


class Melodies:
    def __init__(self):
        self._max_volume = 32_768
        self._volume = int(self._max_volume / 4)

        self._available_melodies = ["Star Trek Intro", "Silent Night", "Pacman", "Ode an die Freude", "Star Wars theme"]
        self._index = decider("Choose which song you want to play", *self._available_melodies)

        self._button = Pin(2, Pin.IN, Pin.PULL_UP)
        # buzzer.irq(handler=self.change_volume, trigger=Pin.IRQ_RISING)
        # self._button.irq(handler=lambda x: self.change_volume(), trigger=Pin.IRQ_RISING)

    def run(self):
        set_volume(self._volume)
        playsong(melody[self._index - 1])

    def change_volume(self):
        self._volume = (self._volume + int(self._max_volume / 4)) % self._max_volume
        set_volume(self._volume)



