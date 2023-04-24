# -*- coding: utf-8 -*-

def intInput(message):
    while (True):
        try:
            value = input(message)

            maxLen = 5
            if value[0] == "-":
                maxLen += 1

            if not (len(value) == maxLen) or value[0] == "0":
                raise ValueError

            value = int(value)

            break
        except ValueError:
            print("The value should be int with 5 digits (signed or unsigned)")

    return value
    while (True):
        value = floatInput(message)
        if value <= 0:
            print("The value should be greater than zero")
        else: break

    return value

while (True):
    number = intInput("Please enter a number with 5 digits (signed or unsigned): ")

    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    thousands = (number // 1000) % 10
    thousandsTens = (number // 10000) % 10

    try:
        result = ((tens ** ones) * hundreds) / (thousandsTens - thousands)
    except ZeroDivisionError:
        print("Divizion by zero error occuried. Please try to chose another number where sub between thousands tens and thousands are greater than zero.")

        continue

    print("Result: %s" % (result))
    
    break