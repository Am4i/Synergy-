# -*- coding: utf-8 -*-

def pluralizeRuWord(num, word):
    if num % 10 == 1 and num % 100 != 11:
        return word
    elif num % 10 in (2, 3, 4) and num % 100 not in (12, 13, 14):
        return word + 'а'
    else:
        return word + 'ов'

petDictionary = {}

def intInput(message):
    while (True):
        try:
            value = int(input(message))

            break
        except ValueError:
            print("The value should be int")

    return value

def strInput(message):
    while (True):
        try:
            value = str(input(message))

            if not value: raise ValueError

            break
        except ValueError:
            print("The value shouldn't be blank")

    return value

def pluralizeWord(num, word):
    result = word

    if not num == 1:
        result += 's'

    return result


petDictionary[strInput("Please enter the nickname of pet: ")] = {
    "type": strInput("Please enter the type of pet: "),
    "age": intInput("Please enter the age of pet: "),
    "hostName": strInput("Please enter the name of the host: ")
}

for petNickname in petDictionary.keys():
    petInfo = list(petDictionary[petNickname].values())
    petInfo.insert(1, petNickname)
    petInfo.insert(3, pluralizeWord(petInfo[2], "year"))


    print ("""This is a %s with nickname "%s". Pet's age is: %s %s. Host's name is: %s.""" % (*petInfo, ))