inputFile = open("Day9Input", "r")
inputData = inputFile.readlines()
strippedInputData = [int(x[:-1]) for x in inputData]
inputData = strippedInputData

setFound = False
targetNumber = 0

for index in range(25,len(inputData)):
    sumOfPrior = False
    preamble = inputData[index-25:index]
    preamble.sort()
    lowerBound = 0
    upperBound = 24
    while lowerBound < upperBound:
        if preamble[lowerBound] + preamble[upperBound] < inputData[index]:
            lowerBound = lowerBound + 1
        if preamble[lowerBound] + preamble[upperBound] > inputData[index]:
            upperBound = upperBound - 1
        if preamble[lowerBound] + preamble[upperBound] == inputData[index]:
            sumOfPrior = True
            break
    if sumOfPrior == False:
        targetNumber = inputData[index]


length = 2

while setFound == False:
    for index in range(len(inputData)-length):
        testSet = inputData[index:index+length]
        if sum(testSet) == targetNumber:
            print(min(testSet) + max(testSet))
            setFound = True
            break
    length = length + 1

