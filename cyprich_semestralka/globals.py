class Globals:
    MAX_PWM: int = 32768
    brightness: float = 0.5  # 0-1
    volume: float = 0.005 # 0-1
    speed: float = 1  # speed in seconds
    ratio: int = 5  # ratio between on and off on led/buzzer during level
    speed_up_levels: int = 3

    @staticmethod
    def speed_up():
        if Globals.speed < 0.1:
            Globals.speed = 0.1
        else:
            Globals.speed *= 0.9


    @staticmethod
    def reset_speed():
        Globals.speed = 1  # TODO hard-typed value
