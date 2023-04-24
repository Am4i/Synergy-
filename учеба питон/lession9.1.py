# -*- coding: utf-8 -*-

numberList = {}

def intInput(message, maxSize):
    while (True):
        try:
            value = int(input(message))

            if abs(value) > maxSize: raise ValueError

            break
        except ValueError:
            print("The value should be int (1 ≤ N ≤ %s) by module" % (maxSize))

    return value

def naturalIntInput(message, maxSize):
    while (True):
        try:
            value = intInput(message, maxSize)

            if value <= 0 or value > maxSize: raise ValueError

            break
        except ValueError:
            print("The value should be natural number (1 ≤ N ≤ %s)" % (maxSize))

    return value

elementsCount = naturalIntInput("Please enter the elements count: ", 100000)
for i in range(elementsCount):
    numberList[intInput("[%s] Please enter a int: " % (i + 1), 2*10e9)] = None

print ("Unique elements count: %s" % len(numberList))