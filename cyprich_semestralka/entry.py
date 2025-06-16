"""Entry.

Entry represents one color (RGB tuple), frequency and color
representation (string).
"""


class Entry:
    """Enum class to represent different entries.

    One entry consists of color (RGB tuple), frequency, and string
    representation. Each value in color tuple can range from 0 to 255.
    Frequency ranges depending on buzzer capacities. String
    representation is the first letter of color, e.g. 'r' for red color.
    """

    # RGB values, frequency, string representation
    RED = ((255, 0, 0), 440, "r")
    GREEN = ((0, 255, 0), 466, "g")
    BLUE = ((0, 0, 255), 494, "b")
    YELLOW = ((255, 255, 0), 523, "y")

    @staticmethod
    def get_values() -> list:
        """Get list of all values to iterate through."""
        return [Entry.RED, Entry.GREEN, Entry.BLUE, Entry.YELLOW]

    @staticmethod
    def get_string_representations():
        """Get string representations of all entries."""
        return [i[2] for i in Entry.get_values()]
