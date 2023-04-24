# -*- coding: utf-8 -*-

import re

def strInput(message):
    while (True):
        try:
            value = str(input(message))

            if len(value) > 1000 or not value: raise ValueError

            break
        except ValueError:
            print("The value should be a string (max length <= 1000, shouldn't be blank)")

    return value

word = strInput("Please enter the string: ")

print (re.sub(' +', ' ', word))