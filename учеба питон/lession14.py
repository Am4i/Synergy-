# -*- coding: utf-8 -*-

def printList(a: list) -> None:
    if a:
        print(a[0])
        printList(a[1:]) 
    else: print("End of the list")

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

printList(a)