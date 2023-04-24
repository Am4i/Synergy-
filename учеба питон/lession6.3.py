# -*- coding: utf-8 -*-

oddList = []

def intInput(message):
    while (True):
        try:
            value = int(input(message))

            break
        except ValueError:
            print("The value should be int")

    return value


a = intInput("[A] Please enter a int number: ")
while (True):
    b = intInput("[B] Please enter a int number: ")
    if b < a: print ("Value should be less or equal to A value")
    else: break

for i in range(a, b + 1):
    if i % 2 == 0: oddList.append(i)

print("Odd numbers: %s" % (" ".join(map(str, oddList))))