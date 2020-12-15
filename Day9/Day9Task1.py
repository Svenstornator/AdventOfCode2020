inputFile = open("Day9Input", "r")
inputData = inputFile.readlines()
strippedInputData = [int(x[:-1]) for x in inputData]
inputData = strippedInputData

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
        print(inputData[index])
