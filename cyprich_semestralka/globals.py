"""Global variables and constants."""


class Globals:
    """Class to wrap all needed global variables and constants."""

    brightness: float = 0.5  # 0-1
    volume: float = 0.01  # 0-1
    MAX_VOLUME_PWM: int = 32768
    SPEED_MAIN: float = 1  # speed of MainLED in seconds
    SPEED_SERIAL: float = 0.15  # speed of SerialLED in seconds
    RATIO: int = 5  # ratio between on and off on led/buzzer during level
    SPEED_UP_LEVELS: int = 2  # how many levels between speed up
    DATABASE_LINK: str = (
        "https:"
        "//vvs-semestralka-a9ec0-default-"
        "rtdb.europe-west1.firebasedatabase.app/")

    @staticmethod
    def speed_up():
        """Rise the speed up."""
        if Globals.SPEED_MAIN < 0.1:
            Globals.SPEED_MAIN = 0.1
        else:
            Globals.SPEED_MAIN *= 0.9

    @staticmethod
    def reset_speed():
        """Reset the speed."""
        Globals.SPEED_MAIN = 1
