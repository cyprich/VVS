import time
from machine import Pin


class Button:
    def __init__(self, pin: int):
        self._p: Pin = Pin(pin, Pin.IN, Pin.PULL_UP)
        self._delay: float = 0.1

    def get_value(self) -> bool:
        if not self._p.value():
            time.sleep(self._delay)
            return not self._p.value()

        time.sleep(self._delay)
        return False
