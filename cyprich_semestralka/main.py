import time

from cyprich_semestralka.manager import Manager
from cyprich_semestralka.website import Website
from cyprich_semestralka.ap import AP


def main():
    Manager.AP.init("cyprich-esp32")
    Manager.load_highscore()

    website = Website()
    website.run()


if __name__ == '__main__':
    main()