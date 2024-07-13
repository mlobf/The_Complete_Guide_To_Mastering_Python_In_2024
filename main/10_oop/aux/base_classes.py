"""Base Class"""


class Lamp:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color

    def turn_on(self):
        """Ligando"""
        print(self.model, "is turned on")

    def turn_off(self):
        """Desligando"""
        print(self.model, "is turned off")

    def describe(self):
        """Descrevendo"""
        print(f"Lamp: {self.model} ({self.color})")


class Animal:
    """A simple Animal class"""

    tricks: list[str] = []

    def __init__(self, name):
        self.name = name

    def make_trick(self, trick_name: str):
        """Simple trick"""
        self.tricks.append(trick_name)
