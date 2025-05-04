from cyprich_uloha3.ap import AP
from cyprich_uloha3.website import Website
from machine import lightsleep

def main():
    sleep_ms = 2000
    lightsleep(sleep_ms)

    ap = AP()
    ap.ask()

    website = Website()
    website.run()

    while True:
        try:
            pass

        except KeyboardInterrupt:
            ap.deinit()
            break


if __name__ == '__main__':
    main()