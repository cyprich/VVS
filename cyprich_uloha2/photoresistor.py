from machine import Pin, ADC, PWM, Timer
from cyprich_uloha2.utils import inputer


# MAX_PHOTO_VALUE = 65535

class Photoresistor:
    def __init__(self):
        self._photo: ADC = ADC(Pin(3), atten=ADC.ATTN_11DB)
        self._MAX_VALUE: int = 65535

    def get_value(self) -> int:
        return self._photo.read_u16()

    def get_percent(self) -> float:
        return self.get_value() / self._MAX_VALUE


class RGB:
    def __init__(self):
        self._r: PWM = PWM(21, freq=120, duty_u16=0)
        self._g: PWM = PWM(11, freq=120, duty_u16=0)
        self._b: PWM = PWM(10, freq=120, duty_u16=0)

        self._MAX_VALUE = 65535


    def _calculate_colors(self, percent: float) -> tuple[int, int, int]:
        result: list[int] = []

        r: int = 0
        g: int = 0
        b: int = 0

        if percent < 0.33:
            local_percent = percent * 3
            r = int((1 - local_percent) * self._MAX_VALUE)
            g = int(local_percent * self._MAX_VALUE)
            b = int(0)
        elif 0.33 <= percent < 0.66:
            local_percent = (percent - 0.33) * 3
            r = int(0)
            g = int((1 - local_percent) * self._MAX_VALUE)
            b = int(local_percent * self._MAX_VALUE)
        else:
            local_percent = (percent - 0.66) * 3
            r = int(local_percent * self._MAX_VALUE)
            g = int(0)
            b = int((1 - local_percent) * self._MAX_VALUE)

        return r, g, b


    def set_color(self, percent: float) -> None:
        values = self._calculate_colors(percent)

        self._r.duty_u16(values[0])
        self._g.duty_u16(values[1])
        self._b.duty_u16(values[2])

    def deinit(self):
        self._r.deinit()
        self._g.deinit()
        self._b.deinit()


def stop(timer: Timer, cancel_timer: Timer, rgb: RGB):
    timer.deinit()
    rgb.deinit()
    cancel_timer.deinit()


def main():
    rgb = RGB()
    photo = Photoresistor()

    user = inputer("How many seconds do you want this effect to last", 1, 61)
    time_coef = 2  # timers only last for half of given time, for unknown reasons

    timer = Timer(0)
    timer.init(period=100, mode=Timer.PERIODIC, callback=lambda _: rgb.set_color(photo.get_percent()))

    cancel_timer = Timer(2)
    cancel_timer.init(period=user*1000*time_coef, mode=Timer.ONE_SHOT, callback=lambda _: stop(timer, cancel_timer, rgb))


if __name__ == '__main__':
    main()