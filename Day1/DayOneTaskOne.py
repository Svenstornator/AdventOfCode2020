# The Goal of this task is to find the product of two numbers that have the sum of 2020

inputFile = open("DayOneTaskOneInput.txt", "r")
inputData = inputFile.readlines()
strippedInputData = [int(x[:-1]) for x in inputData]
inputData = strippedInputData

sumGoal = 2020
half = 0
underHalf = []
overHalf = []

for inputValue in inputData:
    if inputValue == sumGoal/2:
        half = half+1
        if half > 1:
            result = (sumGoal/2)**2
            print(result)
    elif inputValue < sumGoal/2:
        underHalf.append(inputValue)
    else:
        overHalf.append(inputValue)


for inputUnderHalf in underHalf:
    for inputOverHalf in overHalf:
        if inputOverHalf + inputUnderHalf == sumGoal:
            result = inputOverHalf * inputUnderHalf
            print(result)
