import network
import binascii
import time

from cyprich_uloha4.configuration import Configuration


class WiFi:
    def __init__(self):
        self._nic = network.WLAN(network.STA_IF)
        self._nic.active(True)
        
    
    def scan_networks(self):
        print("Scanning available networks...")
        scanning = self._nic.scan()
        open_ssids = []

        print("List of available networks:")
        print(f"\t{'SSID':30} {'MAC':15} {'RSSI':6} Is open?")
        for i in scanning:
            print(f"\t{i[0].decode():30} {binascii.hexlify(i[1]).decode():15} {i[3]:6} {'open' if i[4]==0 else ''}")
            if i[4] == 0:
                open_ssids.append(i[0].decode())
        
    def connect_to_network(self) -> bool:
        if self._nic.isconnected():
            self._nic.disconnect()

        if Configuration.ssid == "":
            ssid = input("\nEnter SSID: ").strip(" ")
            password= input("Enter password: ")

            Configuration.ssid = ssid
            Configuration.password = password
        
        self._nic.connect(Configuration.ssid, Configuration.password)

        print("Trying to connect", end='')
        counter: int = 0
        while not self._nic.isconnected() and counter < 10:
            time.sleep(1)
            counter += 1
            print(".", end="")
            
        if self._nic.isconnected():
            print("\nConnected!")
            values = self._nic.ifconfig()
            print(f"\tIP:      {values[0]}")
            print(f"\tMask:    {values[1]}")
            print(f"\tGateway: {values[2]}")
            print(f"\tDNS:     {values[3]}")

            return True

        else:
            print("Connection timeout, failed to connect...")
            return False


    def disconnect(self):
        self._nic.disconnect()

    def deinit(self):
        self._nic.active(False)


def main():
    wifi = WiFi()	
    wifi.scan_networks()
    wifi.connect_to_network()


if __name__ == "__main__":
    main()

