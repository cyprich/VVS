import os
from microdot.microdot import Microdot, Response
from microdot.utemplate import Template

class Website:
    def __init__(self):
        # creating app
        self._app = Microdot()
        os.chdir("templates")
        try:
            os.remove("webpage_html.py")
        except OSError:
            pass
        os.chdir("/")
        self._webpage = Template("webpage.html")
        Response.default_content_type = "text/html"

        # defining variables
        self._page_vars = {
            "variable_parameter_1": "hello",
            "variable_html": "",
            "variable_css": "",
            "variable_c": "checked",
        }

        self._endpoints()

    def run(self, port: int = 80):
        self._app.run(port=port)

    def _endpoints(self):
        @self._app.route("/")
        async def index(request):
            return self.generate_webpage()


    def generate_webpage(self):
        return self._webpage.render(
            parameter1 = self._page_vars["variable_parameter_1"],
            fplf_html = self._page_vars["variable_html"],
            fplf_css = self._page_vars["variable_css"],
            fplf_C = self._page_vars["variable_c"],
        )

