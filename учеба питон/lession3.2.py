# -*- coding: utf-8 -*-

def floatInput(message):
    while (True):
        try:
            value = float(input(message))
            break
        except ValueError:
            print("The value should be int or float")

    return value

def signedFloatInput(message):
    while (True):
        value = floatInput(message)
        if value <= 0:
            print("The value should be greater than zero")
        else: break

    return value

