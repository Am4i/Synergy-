def factorial(x):
    # Вычисление факториала числа x
    nx = 1
    for i in range(x):
        nx *= i + 1
    return nx

def listFactorialNumbers(x):
    # Создание списка факториалов чисел от факториала числа x до 1
    numbers = factorial(x)
    arr = list()
    for i in range(numbers, 0, -1):
        arr.append(factorial(i))
    return arr

# Вычисление и вывод факториала числа 3
print(factorial(3))

# Создание и вывод списка факториалов чисел от факториала числа 3 до 1
print(listFactorialNumbers(3))
