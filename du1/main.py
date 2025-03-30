from du1.rgb import RGB
from du1.flow import Flow
from du1.melody import Melodies
from du1.utils import decider

options = {
    1: RGB,
    2: Flow,
    3: Melodies
}


def main():
    print("\n--- Assignment 1 ---")

    while True:
        user = decider("\nChoose what to do", "Turn on 1 from 7 basic colors", "Smooth RGB transition", "Play melody", "Exit")

        if user == 4:
            print("Have a nice day! :)")
            break

        option = options[user]()
        option.run()

if __name__ == '__main__':
    main()