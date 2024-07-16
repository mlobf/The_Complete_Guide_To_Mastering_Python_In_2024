"""Uso de classes """

from aux.base_classes import Lamp, Animal,Fruit,Car

if __name__ == "__main__":
    """
    print('-'*79)
    aladim = Lamp("Led", "Vermelha")
    aladim.turn_on()
    aladim.turn_off()
    aladim.describe()
    print('-'*79)
    cat = Animal("Tiao")
    dog = Animal("Dog")
    print('-'*79)
    cat.make_trick("Dar a pata")
    cat.make_trick("Comer pate")
    cat.make_trick("Dormir no sofa tiao")
    dog.make_trick("Dormir no sofa dog")
    cat.make_trick("Brincar com o fio")
    print('-'*79)
    print(cat.tricks)
    print(dog.tricks)
    # Ambas as instancias dividem a lista da variavel  de Classe
    print('-'*79)
    cat.name = "Miau"
    print(cat.name)
    print('-'*79)
    banana = Fruit("banana",20.0)
    print(banana.name)
    print(banana._calories)
    banana.name = "mela"
    """
    car:Car = Car("BMW","Blue")
    print(car)
    print(car.__repr__())




