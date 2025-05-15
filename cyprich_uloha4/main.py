import time

from cyprich_uloha4.config_mode import ConfigMode
from cyprich_uloha4.iot_mode import IotMode
from cyprich_uloha4.utils import decider
from external_libraries.hcsr04 import HCSR04


def main():
    mode: int = decider("Which mode do you want to enter?", "Configuration mode", "IoT mode")
    config_mode = ConfigMode()
    iot_mode = IotMode()
    modes = [config_mode, iot_mode]

    modes[mode - 1].run()



if __name__ == "__main__":
    main()