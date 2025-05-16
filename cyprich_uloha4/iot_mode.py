import sys
import time

from cyprich_uloha4.configuration import Configuration
from cyprich_uloha4.wifi import WiFi
from external_libraries.hcsr04 import HCSR04
import firebase.firebase_library.ufirebase as firebase

class IotMode:
    def __init__(self):
        self._wifi = WiFi()

        firebase.setURL(Configuration.db_url)

        self._ultrasound = HCSR04(Configuration.trigger_pin, Configuration.echo_pin)

    def run(self):
        self.config_wifi()

        print("\nRunning IoT mode")
        print(f"Measuring distance every {Configuration.measure_interval} seconds and sending to Firebase")
        print(f"Firebase field name: {Configuration.db_field}")
        print(f"HCSR04 Pin numbers: Tigger={Configuration.trigger_pin}, Echo={Configuration.echo_pin}")
        print("Press ctrl+c to stop\n")
        while True:
            try:
                value: int = self._ultrasound.distance_mm()
                print(f"Measured distance: {value} mm")

                print("\tSending to Firebase")
                firebase.addto(Configuration.db_field, value)

                interval = Configuration.measure_interval
                print(f"\tMeasuring again in {interval}", end='')
                time.sleep(1)
                for i in range(interval - 1):
                    print(f", {interval - i - 1}", end='')
                    time.sleep(1)
                print("\n")

            except KeyboardInterrupt:
                print("\n\nStopping...")
                break
                
        self._wifi.disconnect()

    def config_wifi(self):
        self._wifi.scan_networks()

        while True:
            try:
                if self._wifi.connect_to_network():
                    break
                else:
                    print("Try again or press ctrl+c to stop and exit program")
            except KeyboardInterrupt:
                sys.exit(1)

    def stop(self):
        self._wifi.disconnect()
        self._wifi.deinit()
