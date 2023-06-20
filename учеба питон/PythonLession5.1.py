
number = int(input("Введите целое число: "))


if number == 0:
    print("Нулевое число")
else:
    
    if number < 0:
        sign = "отрицательное"
    else:
        sign = "положительное"

    
    if number % 2 == 0:
        parity = "четное"
    else:
        parity = "нечетное"

    
    if parity == "четное":
        print(sign, parity, "число")
    else:
        print("Число не является четным")
