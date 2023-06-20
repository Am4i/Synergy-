A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))

for num in range(A, B+1):
    if num % 2 == 0:
        print(num, end=" ")