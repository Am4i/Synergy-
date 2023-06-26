# Создание пустого словаря pets
pets = {}

# Ввод информации о питомце
name = input("Введите имя питомца: ")
animal_type = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

# Создание словаря с информацией о питомце
pet_info = {
    'Вид питомца': animal_type,
    'Возраст питомца': age,
    'Имя владельца': owner_name
}

# Добавление словаря с информацией о питомце в словарь pets
pets[name] = pet_info

# Обработка склонения слова "год"
if age == 1:
    age_string = "1 год"
elif 1 < age < 5:
    age_string = f"{age} года"
else:
    age_string = f"{age} лет"

# Формирование строки с информацией о питомце
info_string = f"Это {animal_type} по кличке \"{name}\". Возраст питомца: {age_string}. Имя владельца: {owner_name}"

# Вывод информации о питомце
print(info_string)


