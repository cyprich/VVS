"""Semester project from subject "Vyvoj vstavanych systemov".

Author: Peter Cyprich, 2025
"""
from cyprich_semestralka.manager import Manager
from cyprich_semestralka.website import Website


def main():
    """Run the program."""
    Manager.AP.init("cyprich-esp32")
    Manager.load_highscore()

    try:
        website = Website()
        website.run()

        while True:
            pass

    except Exception as e:
        print(e)

    finally:
        Manager.deinit()


if __name__ == '__main__':
    main()
