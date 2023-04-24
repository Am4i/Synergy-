# -*- coding: utf-8 -*-

# We are using it as a keys because it works faster than search in array elements + it guarantee unique by values
VOWELS_LIST = {"a": None, "e": None, "i": None, "o": None, "u": None, "y": None} 

vowels = {}
consonants = {}

def inLatin(string):
    try:
        string.encode(encoding = "utf-8").decode("ascii")
    except UnicodeDecodeError:
        return False
    else:
        return True

def wordInput(message):
    while (True):
        try:
            value = str(input(message))

            for char in value: 
                if not char.isalpha(): 
                    raise ValueError

            if not value.islower() or not inLatin(value):
                raise ValueError

            break
        except ValueError:
            print("The value should be a string in lowercase (only latin symbols allowed)")

    return value

word = wordInput("Please enter a a string in lowercase (only latin symbols allowed): ")

for char in word:
    if char in VOWELS_LIST:
        vowels[char] = (vowels[char] if char in vowels else 0) + 1
    else: consonants[char] = (consonants[char] if char in consonants else 0) + 1

print("Vowels counts: %s" % (', '.join(f'{key}: {value}' for key, value in vowels.items())))
print("Consonants count: %s" % (len(consonants)))