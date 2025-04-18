import neopixel
from machine import Pin
from cyprich_uloha2.utils import inputer, rgb_inputer


class SerialLed:
    def __init__(self, led_number: int = 3):
        self._pin_number = 8
        self._count = led_number
        self._np = neopixel.NeoPixel(Pin(self._pin_number), self._count)


    def set_single(self, led_number: int, value: tuple[int, int, int]) -> None:
        print(f"setting led {led_number} to {value}")
        self._np[led_number] = value
        self._np.write()


    def set(self, count, value:tuple[int, int, int]) -> None:
        for i in range(count):
            self.set_single(i, value)


def main():
    count = inputer("How many leds you want to change?", 1, 4)
    values = rgb_inputer("Enter color values for LEDs")

    np = SerialLed(count)
    np.set(count, values)


if __name__ == '__main__':
    main()