inputFile = open("Day10Input", "r")
inputData = inputFile.readlines()
strippedInputData = [int(x[:-1]) for x in inputData]
inputData = strippedInputData
inputData.sort()


threeDifferences = 1 # One for your device
oneDifferences = 1 # One for the plug

print(inputData)

index = 0
while index < len(inputData)-1:
    testCable = inputData[index+1]
    joltageDifference = testCable - inputData[index]
    index = index + 1
    if joltageDifference == 1:
        oneDifferences = oneDifferences + 1
    elif joltageDifference == 3:
        threeDifferences = threeDifferences + 1

print(threeDifferences * oneDifferences)
