# -*- coding: utf-8 -*-

"""
Я не стал делать проверку того, что все числа по модулю не первышают (1000000), 
тк в условиях задачи сказано, что числа не могут превышать 10000, таким образом эта проверка не имеет смысла.
"""

numberList = []

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

            if value <= 0 or value > 10000: raise ValueError

            break
        except ValueError:
            print("The value should be natural number (1 ≤ N ≤ 10000)")

    return value

elementsCount = naturalIntInput("Please enter the elements count: ")
for i in range(elementsCount):
    numberList.append(naturalIntInput("[%s] Please enter a natural number: " % (i + 1)))

print("Reversed array: %s" % (", ".join(map(str,numberList[::-1]))))