m = int(input("Введите максимальную массу, которую может выдержать лодка: "))
n = int(input("Введите количество рыбаков: "))

weights = []
for _ in range(n):
    weight = int(input("Введите вес рыбака: "))
    weights.append(weight)

weights.sort()

lightest = 0
heaviest = n - 1
boats = 0

while lightest <= heaviest:
    if weights[lightest] + weights[heaviest] <= m:
        lightest += 1
    heaviest -= 1
    boats += 1

print("Минимальное количество лодок:", boats)