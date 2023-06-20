# вводим слово
word = input("Введите слово: ")

# счетчик гласных букв
vowel_count = 0
consonant_count = 0


for char in word:
    
    char = char.lower()
    
    # проверка гласных букв
    if char in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1
    # проверка на согл букв
    elif char.isalpha():
        consonant_count += 1


if vowel_count == 0 or consonant_count == 0:
    print(False)
else:
    print("Гласных букв:", vowel_count)
    print("Согласных букв:", consonant_count)
