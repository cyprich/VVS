class Globals:
    brightness: float = 0.5  # 0-1
    volume: float = 0.005 # 0-1
    MAX_VOLUME_PWM: int = 32768
    SPEED_MAIN: float = 1  # speed of MainLED in seconds
    SPEED_SERIAL: float = 0.15  # speed of SerialLED in seconds
    RATIO: int = 5  # ratio between on and off on led/buzzer during level
    SPEED_UP_LEVELS: int = 2  # how many levels between speed up

    @staticmethod
    def speed_up():
        if Globals.SPEED_MAIN < 0.1:
            Globals.SPEED_MAIN = 0.1
        else:
            Globals.SPEED_MAIN *= 0.9


    @staticmethod
    def reset_speed():
        Globals.SPEED_MAIN = 1  # TODO hard-typed value
