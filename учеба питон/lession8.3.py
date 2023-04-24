# -*- coding: utf-8 -*-

class Boat:
    def __init__(self, weightCapacity):
        self.weightCapacity = weightCapacity
        self.addedFishersMap = {}

    def addFishersFromList(self, fishersList):
        for fisherNumber, fisherWeight in fishersList.copy().items():
            if fisherWeight <= self.getAvailableCapacity():
                self.addFisher(fisherNumber, fisherWeight)
                fishersList.pop(fisherNumber)

        return fishersList

    def addFisher(self, fisherNumber, fisherWeight):
        self.addedFishersMap[fisherNumber] = fisherWeight

    def getAvailableCapacity(self):
        addedFishersTotalWeight = 0
        for fisherNumber, fisherWeight in self.addedFishersMap.items():
            addedFishersTotalWeight += fisherWeight

        return self.weightCapacity - addedFishersTotalWeight

    def __str__(self):
        return ", ".join(f'{key}: {value}' for key, value in self.addedFishersMap.items())


def intInput(message):
    while (True):
        try:
            value = int(input(message))

            break
        except ValueError:
            print("The value should be int")

    return value

def naturalIntInput(message, maxSize):
    while (True):
        try:
            value = intInput(message)

            if value <= 0 or value > maxSize: raise ValueError

            break
        except ValueError:
            print("The value should be natural number (1 ≤ N ≤ %s)" % (maxSize))

    return value   

boatWeightCapacity = naturalIntInput("Please enter max weight capacity of the boat: ", 10e6)
fishersCount = naturalIntInput("Please enter fishers count: ", 100)
fishersList = {}

for i in range(fishersCount):
    fishersList["Fisher #%s" % (str(i + 1))] = naturalIntInput("[%s] Please enter a fisher weight: " % (i + 1), boatWeightCapacity)

boatsList = []

while len(fishersList) > 0:
    boat = Boat(boatWeightCapacity)
    fishersList = boat.addFishersFromList(fishersList)

    boatsList.append(boat)

print ("Needed boats count: %s" % (len(boatsList)))

for boatNumber, boat in enumerate(boatsList):
    print ("Boat #%s load: %s" % (boatNumber + 1, boat))