import random

def generate_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(random.randint(-100, 100))
        matrix.append(row)
    return matrix

# Создание первой матрицы
matrix1 = generate_matrix(10, 10)

# Создание второй матрицы
matrix2 = generate_matrix(10, 10)

# Сложение матриц
result_matrix = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(matrix1[i][j] + matrix2[i][j])
    result_matrix.append(row)

# Вывод результатов
print("Матрица 1:")
for row in matrix1:
    print(row)

print("\nМатрица 2:")
for row in matrix2:
    print(row)

print("\nРезультирующая матрица:")
for row in result_matrix:
    print(row)
