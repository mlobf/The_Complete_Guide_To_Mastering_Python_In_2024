class Lamp:
    """A simple Lamp class"""

    def __init__(self, name: str, model: int, version: int):
        self.name = name
        self.__model = model  # private
        """Uso: Indica que a variável é estritamente interna
        à classe onde foi definida e não deve ser acessada nem mesmo pelas subclasses."""
        self._version = version  # protected
        """Convenção para indicar que a variável é para uso interno, 
        mas acessível fora da classe."""

    def print_model(self):
        """Simple test off private variables"""
        self.__self_mantenance()
        return print(str(self.__model))

    def __self_mantenance(self):
        """Simple use of private functions"""
        return print(self.name, "is fixing ifself")


class EletricLamp(Lamp):
    """A simple subclass originated from Lamp class"""

    def __init__(self, name: str, model: int, version: int, wattage: int):
        super().__init__(name, model, version)
        self.wattage = wattage

    def do_something(self):
        print("Eletric lamp version is => ", self._version)
