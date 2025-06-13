import random
import time

from cyprich_semestralka.buzzer import Buzzer
from cyprich_semestralka.entry import Entry
from cyprich_semestralka.globals import Globals
from cyprich_semestralka.main_led import MainLED
from cyprich_semestralka.serial_led import SerialLED


class Manager:
    def __init__(self):
        self._main_led: MainLED = MainLED()
        self._serial_led: SerialLED = SerialLED()
        self._buzzer: Buzzer = Buzzer()

        self._entries: list[Entry] = []

    def next_level(self):
        self._entries.append(random.choice(Entry.get_values()))

        if len(self._entries) % Globals.speed_up_levels == 0:
            Globals.speed_up()

        for i in self._entries:
            self._main_led.set(i)
            self._buzzer.play(i)
            time.sleep(Globals.speed / Globals.ratio * (Globals.ratio - 1))

            self._main_led.turn_off()
            self._buzzer.turn_off()
            time.sleep(Globals.speed / Globals.ratio)

        u: str = input("Enter values: ")
        if not self.validate_input(u):
            self.reset_level()

    def reset_level(self):
        self._entries.clear()
        Globals.reset_speed()


    def validate_input(self, user_entries: list[Entry] | str) -> bool:
        entries: list[str] = []

        if isinstance(user_entries, str):
            entries = list(user_entries.strip(" "))
        elif isinstance(user_entries, list):
            entries = [i[2] for i in user_entries]

        for i in range(len(self._entries)):
            try:
                if self._entries[i][2] != entries[i]:
                    raise AssertionError

            except (AssertionError, IndexError):
                self.fail()
                return False

        self.success()
        return True

    def success(self):
        self._serial_led.success()

    def fail(self):
        self._serial_led.fail()

    def deinit(self):
        self._main_led.deinit()
        self._serial_led.deinit()
        self._buzzer.deinit()
