# -*- coding: utf-8 -*-

def intInput(message):
    while (True):
        try:
            value = int(input(message))

            break
        except ValueError:
            print("The value should be int (signed or unsigned)")

    return value

number = intInput("Please enter a int value (signed or unsigned): ")

isSignedNumber = number >= 0
isEvenNumber = number % 2 == 0

print ("You've entered a %s %s number" % ("signed" if isSignedNumber is True else "unsigned", "even" if isEvenNumber is True else "odd"))