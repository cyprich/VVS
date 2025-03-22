import time
from machine import Pin, PWM

r = Pin(21, Pin.OUT)
g = Pin(10, Pin.OUT)
b = Pin(11, Pin.OUT)

def change_leds(t: float = 1, red: int = 0, green: int = 0, blue: int = 0):
    r.value(red)
    g.value(green)
    b.value(blue)

    time.sleep(t)

    r.off()
    g.off()
    b.off()

def cv4():
    print("[Cvicenie 4 - Zadanie 1]")

    while True:
        try:
            inp = int(input("Enter number from range 1 to 8: "))
            if inp not in range(1, 9):
                raise AssertionError

            t = float(input("Enter time: "))

            break

        except ValueError:
            print("[ERROR] You didnt enter a number")

        except AssertionError:
            print("[ERROR] You didnt enter number from range 1 to 8")

        except Exception:
            print("[ERROR] An error occured")

    if inp == 1:
        change_leds(t)
    elif inp == 2:
        change_leds(t, red=1)
    elif inp == 3:
        change_leds(t, green=1)
    elif inp == 4:
        change_leds(t, blue=1)
    elif inp == 5:
        change_leds(t, red=1, green=1)
    elif inp == 6:
        change_leds(t, red=1, blue=1)
    elif inp == 7:
        change_leds(t, green=1, blue=1)
    elif inp == 8:
        change_leds(t, red=1, green=1, blue=1)

