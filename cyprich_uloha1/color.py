"""Class to represent color."""
class Color:
    """Class to represent color."""

    def __init__(self, r: bool, g: bool, b: bool, name: str):
        """Create instance of the class.

        :param r: If red diode is turned on
        :param g: If green diode is turned on
        :param b: If blue diode is turned on
        :param name: Text name of the color
        """
        self.r = r
        self.g = g
        self.b = b
        self.name = name
