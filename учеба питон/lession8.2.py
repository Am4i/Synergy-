# -*- coding: utf-8 -*-

numberList = []

def intInput(message):
    while (True):
        try:
            value = int(input(message))

            break
        except ValueError:
            print("The value should be int")

    return value

def naturalIntInput(message, maxSize):
    while (True):
        try:
            value = intInput(message)

            if value <= 0 or value > maxSize: raise ValueError

            break
        except ValueError:
            print("The value should be natural number (1 ≤ N ≤ %s)" % (maxSize))

    return value    

def naturalIntArrayInputByString(message, elementsCount, elementMaxSize):
    result = []

    while (True):
        try:
            value = str(input(message))

            rawNumberList = value.split()
            for number in rawNumberList:
                number = int(number)

                if number <= 0 or number > elementMaxSize: raise ValueError

                result.append(number)

            if not len(result) == elementsCount: raise ValueError

            break
        except ValueError:
            print("The value should be a string with %s numbers delimited by space. Each number should be 1 ≤ N ≤ %s" % (elementsCount, elementMaxSize))

    return result

elementsCount = naturalIntInput("Please enter the elements count: ", 100000)
numberList = naturalIntArrayInputByString("Please enter a list of numbers: ", elementsCount, 10e9)

print (numberList[-1:] + numberList[:-1])