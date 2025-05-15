import sys
import time

from cyprich_uloha4.wifi import WiFi
from external_libraries.hcsr04 import HCSR04
import firebase.firebase_library.ufirebase as firebase

class IotMode:
    def __init__(self):
        self._wifi = WiFi()
        self._wifi.scan_networks()

        while True:
            try:
                if self._wifi.connect_to_network():
                    break
                else:
                    print("Try again or press ctrl+c to stop and exit program")
            except KeyboardInterrupt:
                sys.exit(1)

        self.database_url = "https://vvs-uloha4-default-rtdb.europe-west1.firebasedatabase.app/"
        firebase.setURL(self.database_url)
        self.database_path = "measured"

        self.tigger_pin = 15
        self.echo_pin = 23
        self._ultrasound = HCSR04(self.tigger_pin, self.echo_pin)
        self.interval: int = 10

    def run(self):
        print("\nRunning IoT mode")
        print(f"Measuring distance every {self.interval} seconds and sending to database")
        print(f"HCSR04 Pins: Tigger={self.tigger_pin}, Echo={self.echo_pin}")
        print("Press ctrl+c to stop\n")
        while True:
            try:
                value: int = self._ultrasound.distance_mm()
                print(f"Measured distance: {value} mm")

                print("\tSending to Firebase")
                firebase.addto(self.database_path, value)

                print(f"\tMeasuring again in {self.interval}", end='')
                time.sleep(1)
                for i in range(self.interval - 1):
                    print(f", {self.interval - i - 1}", end='')
                    time.sleep(1)
                print("\n")

            except KeyboardInterrupt:
                print("\n\nStopping...")
                break
        self._wifi.disconnect()
