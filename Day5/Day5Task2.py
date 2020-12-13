import math

inputFile = open("Day5Input", "r")
inputData = inputFile.readlines()
strippedInputData = [x[:-1] for x in inputData]
inputData = strippedInputData

idList = []

def findboundaries(lowerbound, upperbound, indicators):
    if len(indicators) > 0 and not lowerbound == upperbound:
        indicator = indicators[0]
        indicators = indicators[1:]
        if indicator == "F" or indicator == "L":
            upperbound = math.floor((lowerbound+upperbound)/2)
        elif indicator == "B" or indicator == "R":
            lowerbound = math.ceil((lowerbound+upperbound)/2)
        return findboundaries(lowerbound, upperbound, indicators)
    else:
        return lowerbound



for boardingPass in inputData:
    row = findboundaries(0,128,boardingPass[:-3])
    column = findboundaries(0,7,boardingPass[-3:])
    idList.append(row*8+column)


idList = sorted(idList)

for index in range(1, len(idList)-1):
    if idList[index]+2 == idList[index+1]:
        print(idList[index]+1)

print(idList)