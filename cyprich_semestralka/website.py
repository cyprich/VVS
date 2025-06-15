"""Website module.

Creates website, and makes user to control peripherals (LED's, buzzer,
photoresistor) through web interface with the use of Microdot library.
"""
import os

from cyprich_semestralka.manager import Manager
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
            os.remove("semestralka_html.py")
        except OSError:
            pass
        os.chdir("/")

        # creating new template
        self._webpage = Template("semestralka.html")
        Response.default_content_type = "text/html"

        # defining variables
        self._user_entries: str = ""

        # runs the _endpoints() method to create endpoints
        self._endpoints()

    def _endpoints(self):
        """Define the endpoints for the web server."""
        @self._app.route("/")
        async def index(request):
            """Handle the root endpoint."""
            return self.generate_webpage()

        @self._app.route("/red")
        async def red(request):
            self._handle_click("r")
            return self.generate_webpage()

        @self._app.route("/green")
        async def green(request):
            self._handle_click("g")
            return self.generate_webpage()

        @self._app.route("/blue")
        async def blue(request):
            self._handle_click("b")
            return self.generate_webpage()

        @self._app.route("/yellow")
        async def yellow(request):
            self._handle_click("y")
            return self.generate_webpage()

        @self._app.route("/start")
        async def start(request):
            self._handle_start()
            return self.generate_webpage()

    def _handle_start(self):
        self._user_entries = ""
        Manager.reset_level()
        Manager.next_level()

    def _handle_click(self, color: str):
        if color not in "rgby":
            return

        self._user_entries += color

        if len(self._user_entries) >= Manager.get_current_level_number():
            if Manager.validate_input(self._user_entries):
                self._user_entries = ""
                Manager.next_level()
            else:
                self._handle_start()

    def run(self, port: int = 80):
        """Run the web server.

        Allows user to specify the network port, which is set to 80 by
        default
        """
        self._app.run(port=port)

    def generate_webpage(self):
        """Generate the webpage, uses variables defined in self._page_vars."""
        return self._webpage.render(
            max(Manager.get_current_level_number() - 1, 0),
            Manager.highscore
        )
