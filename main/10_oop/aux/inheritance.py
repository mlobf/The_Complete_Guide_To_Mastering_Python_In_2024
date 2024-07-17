"""Base Class Python Refresh Course inheritance"""


class Animal:
    """An simple Animal class"""

    def __init__(self, name: str):
        self.name = name

    def sleep(self):
        """Simple sleep method"""
        return print(f"Animal {self.name} is sleeping")

    def eat(self):
        """Simple eat method"""
        return print(f"Animal {self.name} is eating")


class Cat(Animal):
    """An simple Cat class"""

    def __init__(self, name: str, weight: float):
        super().__init__(name)
        self.weight = weight

    def meow(self):
        """simple meow method"""
        return print(f'{self.name} says "meow"')

class Dog(Animal):
    """An simple Dog class"""

    def __init__(self, name: str, weight: float):
        super().__init__(name)
        self.weight = weight

    def bark(self):
        """simple bark method"""
        return print(f'{self.name} says "au au au"')




