class Entry:
    RED = ((255, 0, 0), 440, "r")  # RGB values, frequency, string representation
    GREEN = ((0, 255, 0), 466, "g")
    BLUE = ((0, 0, 255), 494, "b")
    YELLOW = ((255, 255, 0), 523, "y")

    @staticmethod
    def get_values() -> list:
        return [Entry.RED, Entry.GREEN, Entry.BLUE, Entry.YELLOW]