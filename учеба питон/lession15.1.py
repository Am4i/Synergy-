# -*- coding: utf-8 -*-

class Transport:
    def __init__(self, name, maxSpeed, mileage):
        self.name = name
        self.maxSpeed = maxSpeed
        self.mileage = mileage

    def __str__(self) -> str:
        return "Название автомобиля: %s Скорость: %s Пробег: %s" % (self.name, self.maxSpeed, self.mileage)

autobus = Transport("Renaul Logan", 180, 12)
print(autobus)