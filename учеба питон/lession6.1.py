# -*- coding: utf-8 -*-

zeroCount = 0

def intInput(message):
    while (True):
        try:
            value = int(input(message))

            break
        except ValueError:
            print("The value should be int")

    return value

def unsignedIntInput(message):
    while (True):
        try:
            value = intInput(message)

            if value < 0: raise ValueError

            break
        except ValueError:
            print("The value should be unsigned")

    return value

number = unsignedIntInput("Please enter a count of numbers: ")
for i in range(number):
    value = intInput("[%s] Please enter a int value: " % (i))
    if value == 0: zeroCount += 1

print ("Zero count: %s" % (zeroCount))