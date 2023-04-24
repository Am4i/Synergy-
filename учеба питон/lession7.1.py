# -*- coding: utf-8 -*-

def strInput(message):
    while (True):
        try:
            value = str(input(message))

            for char in value:
                if not char.isalpha(): raise ValueError


            break
        except ValueError:
            print("The value should be alphabetical string")

    return value

word = strInput("Please enter the word: ")

print ("yes" if word == word [::-1] else "no")