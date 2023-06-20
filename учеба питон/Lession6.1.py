
N = int(input("Введите число N: "))
count = 0
i = 0

while i < N:
    num = int(input("Введите число: "))
    if num == 0:
        count += 1
    i += 1

print("Количество чисел, равных нулю:", count)