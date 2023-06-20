s = input("Введите строку: ")

# Разделяем строку на слова, игнорируя пробелы
words = s.split()

# Соединяем слова с помощью одного пробела
new_string = ' '.join(words)

print(new_string)