import network


class AP:
    def __init__(self):
        self._nic = network.WLAN(network.AP_IF)


    def init(self, ssid: str, password: str):
        if len(password) == 0:
            self._nic.config(essid=ssid, authmode=0)
        else:
            self._nic.config(essid=ssid, authmode=3, password=password)

        print(f"AP created! Default gateway: {self._nic.ifconfig()[2]}")


    def deinit(self):
        self._nic.active(False)


    def ask(self):
        self._nic.active(True)
        while True:
            try:
                ssid: str = input("Enter SSID for your network: ")
                password: str = input("Enter password (min. 8 characters) or leave empty for open network: ")

                if password != "" and len(password) < 8:
                    raise ValueError

                self.init(ssid, password)
                break

            except ValueError:
                print("Password must be at least 8 characters long...")
            except Exception as e:
                print(f"Unexpected error happened...\n{e}")
