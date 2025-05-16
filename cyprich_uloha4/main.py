"""Assignment 4 from subject "Vyvoj vstavanych systemov".

Author: Peter Cyprich
"""
from machine import Pin
from cyprich_uloha4.config_mode import ConfigMode
from cyprich_uloha4.iot_mode import IotMode
from cyprich_uloha4.utils import decider

def handle_config(config_mode: ConfigMode, iot_mode: IotMode):
    """Handle when button is pressed."""
    iot_mode.stop()
    config_mode.stop()

    config_mode.run()
    iot_mode.run()


def main():
    """Run the program."""
    button: Pin = Pin(2, Pin.IN, Pin.PULL_UP)
    button.irq(
        handler=lambda x: handle_config(config_mode, iot_mode),
        trigger=Pin.IRQ_RISING)

    config_mode = ConfigMode()
    iot_mode = IotMode()

    mode: int = decider("Which mode do you want to enter?", "Configuration mode", "IoT mode")
    modes = [config_mode, iot_mode]
    modes[mode - 1].run()


if __name__ == "__main__":
    main()