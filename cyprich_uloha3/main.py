"""Assignment 3 from subject "Vyvoj vstavanych systemov".

Author: Peter Cyprich
"""
from machine import lightsleep
from cyprich_uloha3.ap import AP
from cyprich_uloha3.website import Website


def main() -> None:
    """Run the program.

    :return: None
    """
    sleep_seconds: int = 5
    print(f"Entering sleep for {sleep_seconds} seconds")
    lightsleep(sleep_seconds * 1000)
    print("Woken up from sleep")

    ap: AP = AP()
    ap.ask()

    website: Website = Website()
    website.run()

    while True:
        try:
            pass

        except KeyboardInterrupt:
            ap.deinit()
            break


if __name__ == '__main__':
    main()
