from cyprich_uloha4.ap import AP
from cyprich_uloha4.website import Website


class ConfigMode:
    def __init__(self):
        self._ap = AP()
        self._website = Website()

    def run(self):
        print("\nEntering configurations mode")
        print("Creating new Access Point...")
        self._ap.ask()
        self._website.run()

    def stop(self):
        self._ap.deinit()