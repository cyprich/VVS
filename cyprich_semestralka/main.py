import time

from cyprich_semestralka.manager import Manager
from cyprich_semestralka.website import Website
from cyprich_semestralka.ap import AP


def main():
    # manager = Manager()
    # while True:
    #     manager.next_level()
    #     time.sleep(1)
    ap = AP()
    ap.init("esp32")

    website = Website()
    website.run()

    while True:
        pass

if __name__ == '__main__':
    main()