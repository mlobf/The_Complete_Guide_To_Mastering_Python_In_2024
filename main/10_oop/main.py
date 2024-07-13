"""Uso de classes
"""

from aux.base_classes import Lamp,Animal


if __name__ == "__main__":

    """
    aladim = Lamp("Led", "Vermelha")
    aladim.turn_on()
    aladim.turn_off()
    aladim.describe()
    """

    cat = Animal('Tiao')
    dog = Animal('Dog')
    cat.make_trick('Dar a pata')
    cat.make_trick('Comer pate')
    cat.make_trick('Dormir no sofa tiao')
    dog.make_trick('Dormir no sofa dog')
    cat.make_trick('Brincar com o fio')
    print(cat.tricks)
    print(dog.tricks)
