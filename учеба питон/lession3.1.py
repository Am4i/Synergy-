# -*- coding: utf-8 -*-

class Pet:
    def __init__(self, type, age, nickname):
        self.type = type
        self.age = age
        self.nickname = nickname

    def __str__(self):
        return f"""This is a %s with nickname "%s". Age: %s years.""" % (self.type, self.age, self.nickname)

def intInput(message):
    while (True):
        try:
            value = int(input(message))
            break
        except ValueError:
            print("The value should be int")

    return value

def strInput(message):
    while (True):
        try:
            value = str(input(message))

            if not value: raise ValueError

            break
        except ValueError:
            print("The value shouldn't be blank")

    return value

def ageInput(message):
    while (True):
        value = intInput(message)
        if value <= 0:
            print("The value should be greater than zero")
        else: break

    return value

pet = Pet(
    strInput("Please enter the type of pet: "),
    strInput("Please enter the nickname of pet: "),
    ageInput("Please enter the age of pet: ")
)

print (pet)