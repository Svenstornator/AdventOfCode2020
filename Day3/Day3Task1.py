inputFile = open("Day3Input", "r")
inputData = inputFile.readlines()
strippedInputData = [x[:-1] for x in inputData]
inputData = strippedInputData

rightDistance = len(inputData[0])
countList = []
result = 1

slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

for slope in slopes:
    position = [0, 0]
    count = 0
    while position[1] < len(inputData):
        position[1] = position[1]+slope[1]
        position[0] = position[0]+slope[0]
        while(position[0] > 30):
            position[0] = position[0] - 31
        if position[1] < len(inputData):
            if inputData[position[1]][position[0]] == "#":
                count = count+1
    countList.append(count)

for count in countList:
    result = result*count

print(result)