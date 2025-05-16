"""Configuration mode.

Second part of the assignment. Provides functionality for configuration
"""

from cyprich_uloha4.ap import AP
from cyprich_uloha4.website import Website


class ConfigMode:
    """Configuration mode."""

    def __init__(self):
        """Initialize the Access Point and the Website."""
        self._ap = AP()
        self._website = Website()

    def run(self):
        """Create Access Point and runs Website."""
        print("\nEntering configurations mode")
        print("Creating new Access Point...")
        self._ap.ask()
        self._website.run()

    def stop(self):
        """Stop the Configuration Mode."""
        self._ap.deinit()
