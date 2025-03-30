from machine import Pin

class Button:
    def __init__(self):
        self._but = Pin(2, Pin.IN, Pin.PULL_UP)

