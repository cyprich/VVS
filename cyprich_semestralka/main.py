import time

from cyprich_semestralka.manager import Manager
from cyprich_semestralka.website import Website
from cyprich_semestralka.ap import AP
from cyprich_semestralka.wifi import WiFi


def main():
    Manager.AP.init("cyprich-esp32")
    Manager.load_highscore()

    # TODO
    Manager.connect_to_wifi("", "")

    website = Website()
    website.run()

    while True:
        pass


if __name__ == '__main__':
    main()