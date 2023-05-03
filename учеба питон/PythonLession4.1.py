# Запрашиваем у пользователя длину и ширину прямоугольника
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Вычисляем площадь и периметр прямоугольника
area = length * width
perimeter = 2 * (length + width)

# Выводим результаты на экран
print("Rectangle area: ", area)
print("Rectangle perimeter: ", perimeter)
