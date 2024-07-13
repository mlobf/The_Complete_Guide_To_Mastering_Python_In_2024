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

    def say_hi(self):
        """Simple say hi"""
        print("Say hi")


class Fruit:
    """Simple Fruit Class"""

    def __init__(self, name: str,calories:float):
        """_name is a private variable"""
        self._name = name
        self._calories=calories

    @property
    def name(self):
        print(f"{self._name}is being accessed")
        return self._name

    @name.setter
    def name(self,value):
        print(f"{self._name}is now {value}")
        self._name = value
        return self._name





