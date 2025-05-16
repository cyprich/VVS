"""Website module.

Creates website, and makes user to control peripherals (LED's, buzzer,
photoresistor) through web interface with the use of Microdot library.
"""
import os

from cyprich_uloha4.configuration import Configuration
from cyprich_uloha4.iot_mode import IotMode
from microdot.microdot import Microdot, Response
from microdot.utemplate import Template


class Website:
    """Represents the web interface for controlling peripherals."""

    def __init__(self):
        """Create instance of the class."""
        # creating app
        self._app = Microdot()

        # deleting old template
        os.chdir("templates")
        try:
            os.remove("configuration_html.py")
        except OSError:
            pass
        os.chdir("/")

        # creating new template
        self._webpage = Template("configuration.html")
        Response.default_content_type = "text/html"

        # runs the _endpoints() method to create endpoints
        self._endpoints()

    def _endpoints(self):
        """Define the endpoints for the web server."""
        @self._app.route("/")
        async def index(request):
            """Handle the root endpoint."""
            return self.generate_webpage()

        @self._app.route("/update")
        async def update(request):
            a = request.args
            Configuration.ssid = a["ssid"]
            Configuration.password = a["password"]
            Configuration.db_url = a["url"]
            Configuration.db_field = a["field"]
            Configuration.trigger_pin = int(a["trigger_pin"])
            Configuration.echo_pin = int(a["echo_pin"])
            Configuration.measure_interval = int(a["interval"])

            IotMode().run()

    def run(self, port: int = 80):
        """Run the web server.

        Allows user to specify the network port, which is set to 80 by
        default
        """
        self._app.run(port=port)

    def generate_webpage(self):
        """Generate the webpage, uses variables defined in self._page_vars."""
        return self._webpage.render(
            measure_interval=Configuration.measure_interval,
            ssid=Configuration.ssid,
            password=Configuration.password,
            url=Configuration.db_url,
            field=Configuration.db_field,
            trigger_pin=Configuration.trigger_pin,
            echo_pin=Configuration.echo_pin
        )
