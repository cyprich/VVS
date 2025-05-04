"""Second part/option of the assignment.

Changes the color of RGB LED based on value taken from photoresistor
Uses timers to measure and stop this effect on RGB LED
"""
from machine import Pin, ADC, PWM, Timer
from cyprich_uloha2.utils import inputer


class Photoresistor:
    """Manages photoresistor."""

    def __init__(self) -> None:
        """Create instance of the class."""
        self._photo: ADC = ADC(Pin(3), atten=ADC.ATTN_11DB)
        self._max_value: int = 65535

    def get_value(self) -> int:
        """Read the value on photoresistor in u16 units."""
        return self._photo.read_u16()

    def get_percent(self) -> float:
        """Read the value on photoresistor in percent."""
        return self.get_value() / self._max_value


class RGB:
    """Manages RGB LED diode."""

    def __init__(self) -> None:
        """Create instance of the class."""
        self._r: PWM = PWM(21, freq=120, duty_u16=0)
        self._g: PWM = PWM(11, freq=120, duty_u16=0)
        self._b: PWM = PWM(10, freq=120, duty_u16=0)

        self._max_value: int = 65535

    def _calculate_colors(self, percent: float) -> tuple[int, int, int]:
        """Calculate color for each one of diodes (red, green, blue).

        Color is calculated from value from photoresistor.
        """
        r: int = 0
        g: int = 0
        b: int = 0

        if percent < 0.33:
            local_percent = percent * 3
            r = int((1 - local_percent) * self._max_value)
            g = int(local_percent * self._max_value)
            b = int(0)
        elif 0.33 <= percent < 0.66:
            local_percent = (percent - 0.33) * 3
            r = int(0)
            g = int((1 - local_percent) * self._max_value)
            b = int(local_percent * self._max_value)
        else:
            local_percent = (percent - 0.66) * 3
            r = int(local_percent * self._max_value)
            g = int(0)
            b = int((1 - local_percent) * self._max_value)

        return r, g, b

    def set_color(self, percent: float) -> None:
        """Set color to each one of LEDs (red, green, blue).

        Percent is from value from photoresistor.
        """
        values = self._calculate_colors(percent)

        self._r.duty_u16(values[0])
        self._g.duty_u16(values[1])
        self._b.duty_u16(values[2])

    def deinit(self) -> None:
        """Deinitialize all LEDs (red, green, blue)."""
        self._r.deinit()
        self._g.deinit()
        self._b.deinit()


def stop(timer: Timer, cancel_timer: Timer, rgb: RGB) -> None:
    """Deinitialize timers and RGB LEDs."""
    timer.deinit()
    rgb.deinit()
    cancel_timer.deinit()


def main() -> None:
    """Run the second part of the assignment."""
    rgb = RGB()
    photo = Photoresistor()

    user = inputer("How many seconds do you want this effect to last", 1, 61)

    # timers only last for half of given time for unknown reasons
    time_coef = 2

    timer = Timer(0)
    timer.init(
        period=100,
        mode=Timer.PERIODIC,
        callback=lambda _: rgb.set_color(
            photo.get_percent()))

    cancel_timer = Timer(2)
    cancel_timer.init(
        period=user *
        1000 *
        time_coef,
        mode=Timer.ONE_SHOT,
        callback=lambda _: stop(
            timer,
            cancel_timer,
            rgb))


if __name__ == '__main__':
    main()
