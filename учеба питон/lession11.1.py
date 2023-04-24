# -*- coding: utf-8 -*-

def intInput(message):
    while (True):
        try:
            value = int(input(message))

            break
        except ValueError:
            print("The value should be int")

    return value

def naturalIntInput(message):
    while (True):
        try:
            value = intInput(message)

            if value <= 0: raise ValueError

            break
        except ValueError:
            print("The value should be natural number")

    return value

def factorial(x: int) -> int:
    result = 1

    if not x == 0:
        result = x * factorial(x - 1)
    
    return result

def factorialList(x: int) -> list:
    result = []
    for i in range(x, 0, -1):
        result.append(factorial(i))
    
    return result

number = naturalIntInput("Please enter a natural number: ")
print (factorialList(factorial(number)))