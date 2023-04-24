# -*- coding: utf-8 -*-

MAX_NUMBERS_COUNT = 100000

numberList = []
numberCountDictionary = {}

def intListInputByString(message, elementsCount):
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

numberList = intListInputByString("[A] Please enter a list of numbers: ", MAX_NUMBERS_COUNT)

for number in numberList:
    print ("Number: %s. Has been before: %s" % (number, "Yes" if number in numberCountDictionary else "No"))
    numberCountDictionary[number] = None