"""Website module.

Creates website, and makes user to control peripherals (LED's, buzzer,
photoresistor) through web interface with the use of Microdot library.
"""
import os
from microdot.microdot import Microdot, Response
from microdot.utemplate import Template
from cyprich_uloha3.melodies import melody
from cyprich_uloha3.play import playsong, set_volume
from cyprich_uloha3.rgb_led import RGBLED
from cyprich_uloha3.serial_led import SerialLED
from cyprich_uloha3.photoresistor import Photoresistor


class Website:
    """Represents the web interface for controlling peripherals."""

    def __init__(self):
        """Create instance of the class."""
        # creating app
        self._app = Microdot()

        # deleting old template
        os.chdir("templates")
        try:
            os.remove("webpage_html.py")
        except OSError:
            pass
        os.chdir("/")

        # creating new template
        self._webpage = Template("webpage.html")
        Response.default_content_type = "text/html"

        # initializing peripherals
        self._photoresistor = Photoresistor()
        self._rgbled = RGBLED()
        self._serialled = SerialLED()

        # defining variables
        self._page_vars = {
            "photoresistor_value": self._photoresistor.get_value(),
            "photoresistor_percent": round(
                self._photoresistor.get_percent(),
                2),
            "rgb_r": 0,
            "rgb_g": 0,
            "rgb_b": 0,
            "serial_1_r": 0,
            "serial_1_g": 0,
            "serial_1_b": 0,
            "serial_2_r": 0,
            "serial_2_g": 0,
            "serial_2_b": 0,
            "serial_3_r": 0,
            "serial_3_g": 0,
            "serial_3_b": 0,
            "buzzer": 1,
            "buzzer_volume": 200,
        }

        # runs the _endpoints() method to create endpoints
        self._endpoints()

    def _endpoints(self):
        """Define the endpoints for the web server."""
        @self._app.route("/")
        async def index():
            """Handle the root endpoint."""
            return self.generate_webpage()

        @self._app.route("/photoresistor")
        async def photoresistor():
            """Handle the click on "Update" button next to photoresistor."""
            self._page_vars["photoresistor_value"] = (
                self._photoresistor.get_value())
            self._page_vars["photoresistor_percent"] = round(
                self._photoresistor.get_percent() * 100, 2)
            return self.generate_webpage()

        @self._app.route("/rgb_led_form")
        async def rgb_led_form(request):
            """Handle change of the value of RGB LED diode."""
            values = [int(request.args[i]) /
                      100 for i in ["rgb_r", "rgb_g", "rgb_b"]]
            self._rgbled.set(
                values[0],
                values[1],
                values[2],
            )

            self._page_vars["rgb_r"] = values[0]
            self._page_vars["rgb_g"] = values[1]
            self._page_vars["rgb_b"] = values[2]

            return self.generate_webpage()

        @self._app.route("/serial_form")
        async def serial_form(request):
            """Handle the change of the value of Serial LED diode."""
            fields = [
                f"serial_{i}_{j}" for i in [
                    1, 2, 3] for j in [
                    "r", "g", "b"]]
            values = [int(request.args[i]) / 100 for i in fields]

            self._serialled.set(0, values[0], values[1], values[2])
            self._serialled.set(1, values[3], values[4], values[5])
            self._serialled.set(2, values[6], values[7], values[8])

            for i in range(len(fields)):
                self._page_vars[fields[i]] = int(values[i] * 100)

            return self.generate_webpage()

        @self._app.route("/buzzer_form")
        async def buzzer_form(request):
            """Handle playing melodies with buzzer."""
            self._page_vars["buzzer"] = int(request.args["buzzer"]) - 1
            self._page_vars["buzzer_volume"] = int(
                request.args["buzzer_volume"])

            set_volume(self._page_vars["buzzer_volume"])
            playsong(melody[self._page_vars["buzzer"]])

            return self.generate_webpage()

    def run(self, port: int = 80):
        """Run the web server.

        Allows user to specify the network port, which is set to 80 by
        default
        """
        self._app.run(port=port)

    def generate_webpage(self):
        """Generate the webpage, uses variables defined in self._page_vars."""
        return self._webpage.render(**self._page_vars)
