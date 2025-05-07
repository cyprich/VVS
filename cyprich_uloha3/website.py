import os

from cyprich_uloha3.rgb_led import RGBLED
from microdot.microdot import Microdot, Response
from microdot.utemplate import Template
from cyprich_uloha3.photoresistor import Photoresistor

class Website:
    def __init__(self):
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

        # peripherals
        self._photoresistor = Photoresistor()
        self._rgbled = RGBLED()

        # defining variables
        self._page_vars = {
            "photoresistor_value": self._photoresistor.get_value(),
            "photoresistor_percent": round(self._photoresistor.get_percent(), 2),
            "rgb_r": 0,
            "rgb_g": 0,
            "rgb_b": 0,
        }

        self._endpoints()

    def run(self, port: int = 80):
        self._app.run(port=port)

    def _endpoints(self):
        @self._app.route("/")
        async def index(request):
            return self.generate_webpage()

        @self._app.route("/photoresistor")
        async def photoresistor(request):
            self._page_vars["photoresistor_value"] = self._photoresistor.get_value()
            self._page_vars["photoresistor_percent"] = round(self._photoresistor.get_percent(), 2)
            return self.generate_webpage()

        @self._app.route("/rgb_led_form")
        async def rgb_led_form(request):
            values = [int(request.args[i]) for i in ["rgb_r", "rgb_g", "rgb_b"]]
            self._rgbled.set(
                values[0] / 100,
                values[1] / 100,
                values[2] / 100,
            )

            self._page_vars["rgb_r"] = values[0]
            self._page_vars["rgb_g"] = values[1]
            self._page_vars["rgb_b"] = values[2]

            return self.generate_webpage()


    def generate_webpage(self):
        return self._webpage.render(**self._page_vars)
