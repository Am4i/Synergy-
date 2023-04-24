# -*- coding: utf-8 -*-

zeroCount = 0
naturalDelimieterCount = 0

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

            if value <= 0 or value >= 2e9: raise ValueError

            break
        except ValueError:
            print("The value should be natural number less than 2 billions (x ≤ 2e9)")

    return value

number = naturalIntInput("Please enter a natural number: ")


for i in range(1, number + 1):
    if number % i == 0:
        naturalDelimieterCount += 1

print ("Natural delimiters count: %s" % (naturalDelimieterCount))