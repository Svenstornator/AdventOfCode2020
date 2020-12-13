import math

inputFile = open("Day5Input", "r")
inputData = inputFile.readlines()
strippedInputData = [x[:-1] for x in inputData]
inputData = strippedInputData

idList = []

def findboundaries(lowerbound, upperbound, indicators):
    if len(indicators) > 0 and lowerbound != upperbound:
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


print(max(idList))


