"""Manages peripherals."""
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
    """Manages peripherals."""

    _main_led: MainLED = MainLED()
    _serial_led: SerialLED = SerialLED()
    _buzzer: Buzzer = Buzzer()
    _entries: list[Entry] = []

    AP: AP = AP()
    _WIFI: WiFi = WiFi()
    ssid: str = ""
    password: str = ""

    FILENAME: str = "cyprich_semestralka/highscore.txt"
    highscore: int = 0

    firebase.setURL(Globals.DATABASE_LINK)
    username: str = "DefaultUser"

    @staticmethod
    def next_level():
        """Play next level."""
        Manager._entries.append(random.choice(Entry.get_values()))

        if len(Manager._entries) % Globals.SPEED_UP_LEVELS == 0:
            Globals.speed_up()

        for i in Manager._entries:
            Manager._main_led.set(i)
            Manager._buzzer.play(i)
            time.sleep(
                Globals.SPEED_MAIN /
                Globals.RATIO * (Globals.RATIO - 1))

            Manager._main_led.turn_off()
            Manager._buzzer.turn_off()
            time.sleep(Globals.SPEED_MAIN / Globals.RATIO)

    @staticmethod
    def reset_level():
        """Reset levels to 0."""
        Manager._entries.clear()
        Globals.reset_speed()

    @staticmethod
    def validate_input(user_entries: list[Entry] | str) -> bool:
        """Check if user put in the right values."""
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
        """Level successfully completed."""
        # Serial LEDs and Buzzer
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
        """Level failed."""
        # Serial LEDs and buzzer
        for _ in range(3):
            Manager._serial_led.fail()
            Manager._buzzer.fail()
            time.sleep(
                Globals.SPEED_SERIAL /
                Globals.RATIO * (Globals.RATIO + 1))

            Manager._serial_led.turn_off(True)
            Manager._buzzer.turn_off()
            time.sleep(Globals.SPEED_SERIAL / Globals.RATIO)

        time.sleep(Globals.SPEED_MAIN)

    @staticmethod
    def get_current_level_number() -> int:
        """Get the number of current level."""
        return len(Manager._entries)

    @staticmethod
    def get_wanted_entries() -> str:
        """Get the string representation of wanted user input."""
        return "".join([i[2] for i in Manager._entries])

    @staticmethod
    def deinit():
        """Deinitialize peripherals."""
        Manager._main_led.deinit()
        Manager._serial_led.deinit()
        Manager._buzzer.deinit()
        Manager.AP.deinit()
        Manager._WIFI.disconnect()
        Manager._WIFI.deinit()

    @staticmethod
    def load_highscore():
        """Load highscore from file."""
        try:
            with open(Manager.FILENAME, 'r', encoding="UTF-8") as file:
                Manager.highscore = int(file.read())
        except Exception as e:
            print(e)

    @staticmethod
    def save_highscore():
        """Save highscore to file."""
        try:
            with open(Manager.FILENAME, 'w', encoding="UTF-8") as file:
                file.write(str(Manager.highscore))
        except Exception as e:
            print(e)

    @staticmethod
    def connect_to_wifi(ssid: str | None = None, password: str | None = None):
        """Connect to WiFi."""
        Manager.ssid = ssid
        Manager.password = password
        Manager._WIFI.connect_to_network(ssid, password)

    @staticmethod
    def is_connected_to_wifi() -> bool:
        """If the ESP32 is connected to WiFi."""
        return Manager._WIFI.is_connected()
