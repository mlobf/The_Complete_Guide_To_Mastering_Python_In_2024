"""Uso de classes """

from aux.base_classes import Animal, Fruit, Car
from aux.private_protected import Lamp, EletricLamp
from aux.inheritance import Animal,Cat,Dog

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
    car:Car = Car("BMW","Blue")
    print(car)
    print(car.__repr__())
    apple:Fruit = Fruit("Apple",10)
    apple2:Fruit = Fruit("Apple",10)
    print(apple==apple2)
    car.hello()
    lamp: Lamp = Lamp("Led", 1234, 99933333)
    lamp.print_model()
    eletric_lamp = EletricLamp("Elamp", 10101, 88888,220)
    eletric_lamp.do_something()
    """
    tiao = Cat("tiao",3.00)
    tiao.meow()
    tiao.sleep()

    freud = Dog('freud',5.00)
    freud.bark()


