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
    sleep_ms: int = 2000
    lightsleep(sleep_ms)

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
