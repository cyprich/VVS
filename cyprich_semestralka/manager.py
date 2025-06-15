import random
import time

from cyprich_semestralka.buzzer import Buzzer
from cyprich_semestralka.entry import Entry
from cyprich_semestralka.globals import Globals
from cyprich_semestralka.main_led import MainLED
from cyprich_semestralka.serial_led import SerialLED
from cyprich_semestralka.ap import AP
from cyprich_semestralka.wifi import WiFi
import cyprich_semestralka.ufirebase as firebase


class Manager:
    _main_led: MainLED = MainLED()
    _serial_led: SerialLED = SerialLED()
    _buzzer: Buzzer = Buzzer()
    _entries: list[Entry] = []

    AP: AP = AP()
    _WIFI: WiFi = WiFi()

    FILENAME: str = "cyprich_semestralka/highscore.txt"
    highscore: int = 0

    firebase.setURL("https://vvs-semestralka-a9ec0-default-rtdb.europe-west1.firebasedatabase.app/")


    @staticmethod
    def next_level():
        Manager._entries.append(random.choice(Entry.get_values()))

        if len(Manager._entries) % Globals.SPEED_UP_LEVELS == 0:
            Globals.speed_up()

        for i in Manager._entries:
            Manager._main_led.set(i)
            Manager._buzzer.play(i)
            time.sleep(Globals.SPEED_MAIN / Globals.RATIO * (Globals.RATIO - 1))

            Manager._main_led.turn_off()
            Manager._buzzer.turn_off()
            time.sleep(Globals.SPEED_MAIN / Globals.RATIO)

    @staticmethod
    def reset_level():
        Manager._entries.clear()
        Globals.reset_speed()

    @staticmethod
    def validate_input(user_entries: list[Entry] | str) -> bool:
        entries: list[str] = []

        if isinstance(user_entries, str):
            entries = list(user_entries.strip(" "))
        elif isinstance(user_entries, list):
            entries = [i[2] for i in user_entries]

        for i in range(len(Manager._entries)):
            try:
                if Manager._entries[i][2] != entries[i]:
                    raise AssertionError

            except (AssertionError, IndexError):
                Manager.fail()
                return False

        Manager.success()
        return True

    @staticmethod
    def success():
        for i in range(3):
            Manager._serial_led.success(i)
            Manager._buzzer.success(i)
            time.sleep(Globals.SPEED_SERIAL)
            Manager._serial_led.turn_off(True)
            Manager._buzzer.turn_off()

        # handle highscore
        if Manager.highscore < Manager.get_current_level_number():
            Manager.highscore = Manager.get_current_level_number()
            Manager.save_highscore()

        time.sleep(Globals.SPEED_MAIN)

    @staticmethod
    def fail():
        for i in range(3):
            Manager._serial_led.fail()
            Manager._buzzer.fail()
            time.sleep(Globals.SPEED_SERIAL / Globals.RATIO * (Globals.RATIO + 1))

            Manager._serial_led.turn_off(True)
            Manager._buzzer.turn_off()
            time.sleep(Globals.SPEED_SERIAL / Globals.RATIO)

        time.sleep(Globals.SPEED_MAIN)

    @staticmethod
    def get_current_level_number() -> int:
        return len(Manager._entries)

    @staticmethod
    def get_wanted_entries() -> str:
        return "".join([i[2] for i in Manager._entries])

    @staticmethod
    def deinit():
        Manager._main_led.deinit()
        Manager._serial_led.deinit()
        Manager._buzzer.deinit()

    @staticmethod
    def load_highscore():
        try:
            with open(Manager.FILENAME, 'r') as file:
                Manager.highscore = int(file.read())
        except Exception:
            pass


    @staticmethod
    def save_highscore():
        try:
            with open(Manager.FILENAME, 'w') as file:
                file.write(str(Manager.highscore))
        except Exception:
            pass

    @staticmethod
    def connect_to_wifi(ssid: str | None = None, password: str | None = None):
        Manager._WIFI.connect_to_network(ssid, password)
