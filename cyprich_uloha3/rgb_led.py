"""Control RGB LED."""

from machine import PWM


class RGBLED:
    """Class that controls RGB LED.

    Makes user able to easily set the color.
    """

    def __init__(
            self,
            r_pin_number: int = 21,
            g_pin_number: int = 11,
            b_pin_number: int = 10) -> None:
        """Create instance of the class.

        :param: Number of PIN connected to Red, Green and Blue channels
            respectively
        """
        self._max_duty = 65535
        self._r: PWM = PWM(r_pin_number, freq=120, duty_u16=0)
        self._g: PWM = PWM(g_pin_number, freq=120, duty_u16=0)
        self._b: PWM = PWM(b_pin_number, freq=120, duty_u16=0)

    def get(self) -> tuple[int, int, int]:
        """Return the values of Red, Green and Blue LED's respectively.

        Returns in u16 units
        """
        return self._r.duty_u16(), self._g.duty_u16(), self._b.duty_u16()

    def set(
            self,
            r_percent: float = 0,
            g_percent: float = 0,
            b_percent: float = 0) -> None:
        """Set the values of Red, Green and Blue LED's respectively.

        :param: Value for Red, Green and Blue respectively. Expects
            decimal values in range from 0 to 1, where 1 is fully bright
            LED and 0 is fully dark LED.
        """
        self._r.duty_u16(int(r_percent * self._max_duty))
        self._g.duty_u16(int(g_percent * self._max_duty))
        self._b.duty_u16(int(b_percent * self._max_duty))
