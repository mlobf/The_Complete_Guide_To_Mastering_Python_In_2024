"""Uso de classes
"""

from aux.base_classes import Lamp


if __name__ == "__main__":
    aladim = Lamp('Led',"Vermelha")
    aladim.turn_on()
    aladim.turn_off()
    aladim.describe()
