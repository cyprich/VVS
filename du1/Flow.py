import time
from machine import PWM, Timer

from du1.utils import inputer

class Flow:
    def __init__(self):
        self._max_duty = 65535
        self._r: PWM = PWM(21, freq=120, duty_u16=0)
        self._g: PWM = PWM(11, freq=120, duty_u16=0)
        self._b: PWM = PWM(10, freq=120, duty_u16=0)

    def _change_color(self, r: int, g: int, b: int):
        self._r.duty_u16(r)
        self._g.duty_u16(g)
        self._b.duty_u16(b)

    def run(self):
        speed = 8
        user_time = inputer("How many seconds you want this effect to take?", 1, 6)

        # this did not work
        # tim = Timer(1)
        # tim.init(mode=Timer.ONE_SHOT, period=100, callback=lambda t: self.stop())

        start_time = time.time()

        while time.time() - start_time <= user_time:
            for i in range(0, self._max_duty, speed):
                self._change_color(self._max_duty - i, i, 0)
                if not time.time() - start_time <= user_time:
                    break
            for i in range(0, self._max_duty, speed):
                self._change_color(0, self._max_duty - i, i)
                if not time.time() - start_time <= user_time:
                    break
            for i in range(0, self._max_duty, speed):
                self._change_color(i, 0, self._max_duty - i)
                if not time.time() - start_time <= user_time:
                    break

        self.stop()

    def stop(self) -> None:
        self._r.deinit()
        self._g.deinit()
        self._b.deinit()
