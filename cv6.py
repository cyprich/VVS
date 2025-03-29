import neopixel
import time
from machine import Pin, ADC

class Uloha2:
    def __init__(self, pin: int = 8, count: int = 3):
        self._pin = pin
        self._count = count
        self._np = neopixel.NeoPixel(Pin(pin), count)

    def set(self, led: int, value: tuple[int, int, int]):
        if led not in range(0, self._count) or len(value) != 3:
            raise Exception("Wrong parameters entered")

        self._np[led] = value

    def write(self):
        self._np.write()

    def turn_off(self):
        [self.set(i, (0,0,0)) for i in range(self._count)]
        self.write()

class Uloha3:
    def __init__(self):
        p = ADC(Pin(3), atten=ADC.ATTN_11DB)

        while True:
            val = p.read_u16()
            print(val)

            time.sleep(1)



def main():
    x = Uloha2(8, 3)
    # x.set(0, (127, 255, 0))
    # x.write()
    # time.sleep(5)
    x.turn_off()

    # Uloha3()
    p = ADC(Pin(3), )

    while True:
        print(p.read_u16())
        time.sleep(0.5)