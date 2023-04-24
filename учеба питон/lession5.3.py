# -*- coding: utf-8 -*-

investorList = {"Mike": 0, "Ivan": 0}
investorsTotalFunds = 0
investorsWhoCanInvestCount = 0

def intInput(message):
    while (True):
        try:
            value = int(input(message))

            if value <= 0: raise ValueError

            break
        except ValueError:
            print("The value should be unsigned int")

    return value

minFunds = intInput("Please enter a minimum funds: ")
for investorName in investorList.keys():
    funds = intInput("Please enter %s's funds: " % (investorName))
    investorList[investorName] = funds
    investorsTotalFunds += funds
    if funds >= minFunds: investorsWhoCanInvestCount += 1

if investorsWhoCanInvestCount == len(investorList):
    print ("%s (All investors can invest)" % (investorsWhoCanInvestCount))
elif investorsWhoCanInvestCount > 0:
    for investorName in investorList.keys():
        if investorList[investorName] >= minFunds: print ("%s (can invest)" % (investorName))
elif investorsTotalFunds >= minFunds:
    print ("1 (all investors can invest with eatch other by adding funds as shared invest)")
else:
    print ("0 (no one can invest)")