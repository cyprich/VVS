"""Website module.

Creates website, and makes user to control peripherals (LED's, buzzer,
photoresistor) through web interface with the use of Microdot library.
"""
import os
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

        # initializing peripherals

        # defining variables
        self._page_vars = {}

        # runs the _endpoints() method to create endpoints
        self._endpoints()

    def _endpoints(self):
        """Define the endpoints for the web server."""
        @self._app.route("/")
        async def index(request):
            """Handle the root endpoint."""
            return self.generate_webpage()


    def run(self, port: int = 80):
        """Run the web server.

        Allows user to specify the network port, which is set to 80 by
        default
        """
        self._app.run(port=port)

    def generate_webpage(self):
        """Generate the webpage, uses variables defined in self._page_vars."""
        # return self._webpage.render(**self._page_vars)
        return self._webpage.render()
