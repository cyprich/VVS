from cyprich_uloha2.utils import decider
from cyprich_uloha2.serial_led import main as serial_led
from cyprich_uloha2.photoresistor import main as photoresistor
from cyprich_uloha2.communication import main as communication


def main():
    while True:
        user = decider("Choose what you want to do", "Use serial RGB LEDs", "Use RGB LED with photoresistor", "UART communication", "Exit")

        if user == 1:
            serial_led()
        elif user == 2:
            photoresistor()
        elif user == 3:
            communication()
        else:
            break


if __name__ == '__main__':
    main()