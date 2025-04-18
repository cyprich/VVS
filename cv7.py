import time
from machine import Timer, Pin
from cv5_uloha2 import Button

red = Pin(21, Pin.OUT)
green = Pin(11, Pin.OUT)
blue = Pin(10, Pin.OUT)


class Casovac:
    def __init__(self, cislo: int = 0):
        self._casovac = Timer(cislo)
        self._casovac.init()

    def init(self, *, mode: int = Timer.PERIODIC, period: int = -1, freq: float = -1, callback):
        self._casovac.init(mode=mode, period=period*2, freq=freq/2, callback=callback)

    def deinit(self):
        self._casovac.deinit()


def switch_red():
    red.value(not red.value())

def uloha1():
    casovac = Casovac(0)
    casovac2 = Casovac(2)
    # casovac.init(period=2000, mode=Timer.ONE_SHOT, callback=None)
    casovac.init(freq=1/2, mode=Timer.PERIODIC, callback=lambda _: switch_red())
    casovac2.init(freq=1/10, callback=lambda _: print("Ubehlo 10 sekund"))
    # casovac.init(freq=2, mode=Timer.PERIODIC, callback=switch_red)
    time.sleep(20)
    casovac.deinit()
    casovac2.deinit()

def uloha3():
    # tlacidlo1 = Pin(2, Pin.IN, Pin.PULL_UP)
    # tlacidlo2 = Pin(9, Pin.IN, Pin.PULL_UP)
    tlacidlo1 = Button(2)
    tlacidlo2 = Button(9)

    while True:
        if tlacidlo1.get_value():
            red.value(0)
            green.value(0)
            blue.value(1)
            time.sleep(1)
            red.value(1)
            green.value(1)
            blue.value(0)
            time.sleep(1.5)
            red.value(0)
            green.value(0)
            blue.value(0)
        if tlacidlo2.get_value():
            print("Tlacidlo 2 bolo stlacene")

def uloha4():
    pass


def main():
    print("[CV7]")
    # uloha1()
    # uloha3()
    uloha4()

if __name__ == '__main__':
    main()