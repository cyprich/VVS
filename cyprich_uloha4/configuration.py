"""Variables for configuration."""


class Configuration:
    """Variables for configuration."""

    ssid: str = ""
    password: str = ""

    db_url: str = ("https://vvs-uloha4-default-rtdb."
                   "europe-west1.firebasedatabase.app/")
    db_field: str = "measured"

    trigger_pin: int = 15
    echo_pin: int = 23

    measure_interval: int = 10

    def dummy(self):
        """Added just because of PEP, does nothing."""
        return ""

    def dummy2(self):
        """Added just because of PEP, does nothing."""
        return ""
