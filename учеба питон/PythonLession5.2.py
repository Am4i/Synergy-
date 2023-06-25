word = input("Введите слово: ")

# Переводим слово в нижний регистр для удобства сравнения
word = word.lower()

# Инициализируем переменные для подсчета гласных и согласных
vowels_count = 0
consonants_count = 0

# Перебираем буквы в слове и считаем гласные и согласные
for letter in word:
    if letter in "aeiouy":
        vowels_count += 1
    elif letter.isalpha():
        consonants_count += 1

# Выводим результат
if vowels_count > 0 and consonants_count > 0:
    print(f"Количество гласных: {vowels_count}")
    print(f"Количество согласных: {consonants_count}")
else:
    print(False)
