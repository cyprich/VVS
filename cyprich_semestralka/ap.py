"""Access Point.

Provides functionality to create Wi-Fi Access Point (AP). Allows user to
customize SSID and password of Access Point.
"""
import network


class AP:
    """Access Point.

    Provides functionality to create Wi-Fi Access Point (AP). Allows
    user to customize SSID and password of Access Point.
    """

    def __init__(self):
        """Create instance of the class."""
        self._nic = network.WLAN(network.AP_IF)

    def init(self, ssid: str, password: str | None = None) -> None:
        """Initialize Access Point with given SSID and password.

        Password can be empty for network without password. If the
        password is provided, it has to have at least 8 characters
        """
        self._nic.active(True)

        if password is None or len(password) == 0:
            self._nic.config(essid=ssid, authmode=0)
        else:
            self._nic.config(essid=ssid, authmode=3, password=password)

        print(f"AP created! Default gateway: {self._nic.ifconfig()[2]}")

    def deinit(self) -> None:
        """Deinitialize/Deactivate the Access Point."""
        self._nic.active(False)

    def ask(self) -> None:
        """Guides user through initialization of the Access Point.

        Asks for SSID and password and checks if it's correct.
        """
        while True:
            try:
                ssid: str = input("Enter SSID for your network: ")
                password: str = input(
                    "Enter password (min. 8 characters) "
                    "or leave empty for open network: ")

                if password != "" and len(password) < 8:
                    raise ValueError

                self.init(ssid, password)
                break

            except ValueError:
                print("Password must be at least 8 characters long...")
            except Exception as e:
                print(f"Unexpected error happened...\n{e}")
