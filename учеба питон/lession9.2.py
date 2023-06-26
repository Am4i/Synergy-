# Ввод двух списков чисел
list1 = set(map(int, input().split()))
list2 = set(map(int, input().split()))

# Нахождение пересечения двух списков
intersection = list1 & list2

# Вывод количества чисел, содержащихся одновременно в обоих списках
print(len(intersection))
