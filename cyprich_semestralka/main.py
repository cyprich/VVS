import time

from cyprich_semestralka.manager import Manager


def main():
    manager = Manager()
    while True:
        manager.next_level()
        time.sleep(1)

if __name__ == '__main__':
    main()