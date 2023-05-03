# -*- coding: utf-8 -*-
# We request the length and width of the rectangle from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area and perimeter of the rectangle
area = length * width
perimeter = 2 * (length + width)

# We display the results on the screen
print("Rectangle area: ", area)
print("Rectangle perimeter: ", perimeter)
