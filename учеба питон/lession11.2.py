# -*- coding: utf-8 -*-

class Db:
    def __init__(self) -> None:
        self.db = {}

    def getPet(self, id: int) -> dict:
        if not id in self.db.keys():
            raise Exception("""Record with id "%s" not found""" % id)

        return self.db[id]

    def create(self, petNickname: str, petType: str, petAge: int, petHostName: str) -> None:
        id = 1
        currentIds = self.db.keys()
        if currentIds: id = max(currentIds) + 1
    
        self.db[id] = {}
        self.update(id, petNickname, petType, petAge, petHostName)

    def update(self, id: int, petNickname: str, petType: str, petAge: int, petHostName: str) -> None:
        self.getPet(id)

        self.db[id] = {
            petNickname: {
                "type": petType,
                "age": petAge,
                "hostName": petHostName
            }
        }

    def remove(self, id: int) -> None:
        self.getPet(id)
        self.db.pop(id)

    def print(self, id: int) -> None:
        data = self.getPet(id)
        nickname = list(data.keys())[0]
        data = data[nickname]

        print (
            """This is a %s with nickname "%s". Pet's age is: %s %s. Host's name is: %s.""" 
            % (data["type"], nickname, data["age"], self.pluralizeWord(data["age"], "year"), data["hostName"])
        )

    def pluralizeWord(self, num, word) -> str:
        result = word

        if not num == 1:
            result += 's'

        return result

    def list(self) -> None:
        for id in self.db.keys():
            self.print(id)

db = Db()

while True:
    command = input("Enter command: ")
    tokens = command.split()
    
    try:
        if len(tokens) == 0:
            continue
        if tokens[0] == "create" and len(tokens) == 5:
            db.create(tokens[1], tokens[2], int(tokens[3]), tokens[4])
        elif tokens[0] == "update" and len(tokens) == 6:
            db.update(int(tokens[1]), tokens[2], tokens[3], int(tokens[4]), tokens[5])
        elif tokens[0] == "remove" and len(tokens) == 2:
            db.remove(int(tokens[1]))
        elif tokens[0] == "print" and len(tokens) == 2:
            db.print(int(tokens[1]))
        elif tokens[0] == "list" and len(tokens) == 1:
            db.list()
        elif tokens[0] == "stop":
            break;
        else:
            print("Invalid command or arguments")
    except Exception as e: print(str(e))