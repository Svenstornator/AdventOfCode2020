# The goal of this task is to find the product of three numbers that sum to 2020

inputFile = open("DayOneTaskOneInput.txt", "r")
inputData = inputFile.readlines()
strippedInputData = [int(x[:-1]) for x in inputData]
inputData = strippedInputData

sumGoal = 2020

underThird = []
overThird = []

for inputValue in inputData:
    if inputValue <= sumGoal/3:
        underThird.append(inputValue)
    else:
        overThird.append(inputValue)

# Case 1 : Two numbers under 1/3 one over 1/3
for firstIndex in range(len(underThird)):
    for secondIndex in range(firstIndex + 1, len(underThird)):
        for valueOverThird in overThird:
            if underThird[firstIndex] + underThird[secondIndex] + valueOverThird == sumGoal:
                result = underThird[firstIndex] * underThird[secondIndex] * valueOverThird
                print(result)
                quit()


# Case 2 : Two number over 1/3 and one under
for firstIndex in range(len(overThird)):
    for secondIndex in range(firstIndex + 1, len(overThird)):
        for valueUnderThird in underThird:
            if overThird[firstIndex] + overThird[secondIndex] + valueUnderThird == sumGoal:
                result = overThird[firstIndex] * overThird[secondIndex] * valueUnderThird
                print(result)
                quit()