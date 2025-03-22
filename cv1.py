class Square:
    def __init__(self, a:float):
        self._a: float = a

    def area(self):
        return self._a ** 2

    def circumference(self):
        return self._a * 4

class Rectangle:
    def __init__(self, a: float, b: float):
        self._a: float = a
        self._b: float = b

    def area(self):
        return self._a * self._b

    def circumference(self):
        return self._a * 2 + self._b * 2

class Triangle:
    def __init__(self, a: float, b: float, c: float, h: float):
        self._a: float = a
        self._b: float = b
        self._c: float = c
        self._h: float = h

    def area(self):
        return (self._a * self._h) / 2

    def circumference(self):
        return self._a + self._b + self._c

