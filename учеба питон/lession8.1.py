N = int(input("Введите кол-во массив чисел: "))
numbers = []

# Ввод чисел
for _ in range(N):
    number = int(input("Введите число: "))
    numbers.append(number)

# Переворот массива
reversed_numbers = numbers[::-1]

# Вывод перевернутого массива
for number in reversed_numbers:
    print(number)
