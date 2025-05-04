import network
import time
import binascii


class WiFi:
    def __init__(self):
        self._nic = network.WLAN(network.STA_IF)
        self._nic.active(True)


    def scan(self):
        scanning = self._nic.scan()
        open_ssids = []

        print("List of available networks:")
        print(f"\t{'SSID':30} {'MAC':15} Is open?")
        for i in scanning:
            print(
                f"\t{i[0].decode():30} {binascii.hexlify(i[1]).decode():15} {'open' if i[4] == 0 else ''}")
            if i[4] == 0:
                open_ssids.append(i[0].decode())


    def connect(self) -> bool:
        ssid = input("\nEnter SSID: ").strip(" ")
        password = input("Enter password: ")

        self._nic.connect(ssid, password)

        print("Trying to connect", end='')
        while not self._nic.isconnected():
            time.sleep(0.5)
            print(".", end="")

        print()

        return self._nic.isconnected()


    def disconnect(self):
        self._nic.disconnect()


    def get_ifconfig(self):
        return self._nic.ifconfig()

    def AP(self):
        pass
