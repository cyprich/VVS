from cyprich_semestralka.manager import Manager
from cyprich_semestralka.website import Website


def main():
    Manager.AP.init("cyprich-esp32")
    Manager.load_highscore()

    try:
        website = Website()
        website.run()

        while True:
            pass

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()