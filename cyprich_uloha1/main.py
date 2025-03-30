import time

from cyprich_uloha1.flow import Flow
from cyprich_uloha1.melody import Melody
from cyprich_uloha1.rgb import RGB
from cyprich_uloha1.utils import decider

options = {1: RGB, 2: Flow, 3: Melody}


def main() -> None:
    print("\n--- Assignment 1 ---")

    while True:
        user: int = decider(
            "\nChoose what to do",
            "Turn on 1 from 7 basic colors", "Smooth RGB transition", "Play melody", "Exit"
        )

        if user == 4:
            print("Have a nice day! :)")
            break

        option = options[user]()
        option.run()


if __name__ == '__main__':
    main()
