# -*- coding: utf-8 -*-

MAX_NUMBERS_COUNT = 100000

numberListA = {}
numberListB = {}

def intArrayInputByString(message, elementsCount):
    result = []

    while (True):
        try:
            value = str(input(message))

            rawNumberList = value.split()
            for number in rawNumberList:
                number = int(number)
                result.append(number)

            if len(result) > elementsCount: raise ValueError

            break
        except ValueError:
            print("The value should be a string with maximum %s numbers delimited by space" % (elementsCount))

    return result

numberListA = intArrayInputByString("[A] Please enter a list of numbers: ", MAX_NUMBERS_COUNT)
numberListB = intArrayInputByString("[B] Please enter a list of numbers: ", MAX_NUMBERS_COUNT)

print ("Intersection: %s" % (set(numberListA).intersection(numberListB)))