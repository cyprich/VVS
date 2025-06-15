class Globals:
    MAX_PWM: int = 32768
    brightness: float = 0.5  # 0-1
    volume: float = 0.01 # 0-1
    speed_main: float = 1  # speed in seconds
    speed_serial: float = 0.15
    ratio: int = 5  # ratio between on and off on led/buzzer during level
    speed_up_levels: int = 2  # how many levels between speed up

    @staticmethod
    def speed_up():
        if Globals.speed_main < 0.1:
            Globals.speed_main = 0.1
        else:
            Globals.speed_main *= 0.9


    @staticmethod
    def reset_speed():
        Globals.speed_main = 1  # TODO hard-typed value
