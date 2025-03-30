from machine import Pin
from cyprich_uloha1.color import Color
from cyprich_uloha1.utils import decider

class RGB:
    def __init__(self):
        self._r: Pin = Pin(21, Pin.OUT)
        self._g: Pin = Pin(11, Pin.OUT)
        self._b: Pin = Pin(10, Pin.OUT)

        self._colors: list[Color] = list()
        self._colors.append(Color(True, False, False, "Red"))
        self._colors.append(Color(False, True, False, "Green"))
        self._colors.append(Color(False, False, True, "Blue"))
        self._colors.append(Color(True, True, False, "Yellow"))
        self._colors.append(Color(True, False, True, "Magenta"))
        self._colors.append(Color(False, True, True, "Cyan"))
        self._colors.append(Color(True, True, True, "White"))

    def run(self):
        print("\n--- RGB ---")
        user: int = decider("Choose one from colors to show", *[i.name for i in self._colors]) - 1

        self._r.value(self._colors[user].r)
        self._g.value(self._colors[user].g)
        self._b.value(self._colors[user].b)

        input("Press enter to stop...")
        self.stop()

    def stop(self):
        self._r.off()
        self._g.off()
        self._b.off()
