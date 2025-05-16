"""Handles operations with WiFi."""
import time
import binascii
import network

from cyprich_uloha4.configuration import Configuration


class WiFi:
    """Handle operations with WiFi."""

    def __init__(self):
        """Initialize the network card."""
        self._nic = network.WLAN(network.STA_IF)
        self._nic.active(True)

    def scan_networks(self):
        """Scan available networks."""
        print("Scanning available networks...")
        scanning = self._nic.scan()
        open_ssids = []

        print("List of available networks:")
        print(f"\t{'SSID':30} {'MAC':15} {'RSSI':6} Is open?")
        for i in scanning:
            print(
                f"\t{
                    i[0].decode():30} {
                    binascii.hexlify(
                        i[1]).decode():15} {
                    i[3]:6} {
                        'open' if i[4] == 0 else ''}")
            if i[4] == 0:
                open_ssids.append(i[0].decode())

    def connect_to_network(self) -> bool:
        """Connect to network.

        If Configuration.ssid is empty, it asks user to set the SSID and
        password of WiFi to connect to.
        """
        # disconnect if already connected
        if self._nic.isconnected():
            self._nic.disconnect()

        # ssid and password
        if Configuration.ssid == "":
            ssid = input("\nEnter SSID: ").strip(" ")
            password = input("Enter password: ")

            Configuration.ssid = ssid
            Configuration.password = password

        # connecting
        self._nic.connect(Configuration.ssid, Configuration.password)

        # waiting to connect for 10 seconds
        print("Trying to connect", end='')
        counter: int = 0
        while not self._nic.isconnected() and counter < 10:
            time.sleep(1)
            counter += 1
            print(".", end="")

        # prints IP, mask, ... if connected
        if self._nic.isconnected():
            print("\nConnected!")
            values = self._nic.ifconfig()
            print(f"\tIP:      {values[0]}")
            print(f"\tMask:    {values[1]}")
            print(f"\tGateway: {values[2]}")
            print(f"\tDNS:     {values[3]}")

            return True

        # prints fail message when not connected
        print("Connection timeout, failed to connect...")
        return False

    def disconnect(self):
        """Disconnect."""
        self._nic.disconnect()

    def deinit(self):
        """Deinitialize network card."""
        self._nic.active(False)
