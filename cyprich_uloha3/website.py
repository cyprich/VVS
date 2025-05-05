import os
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

        # from previous homeworks
        self._photoresistor = Photoresistor()

        # defining variables
        self._page_vars = {
            "photoresistor_value": self._photoresistor.get_value(),
            "photoresistor_percent": round(self._photoresistor.get_percent(), 2),
            "r": 0,
            "g": 0,
            "b": 0,
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


    def generate_webpage(self):
        print(self._page_vars)
        return self._webpage.render(**self._page_vars)
