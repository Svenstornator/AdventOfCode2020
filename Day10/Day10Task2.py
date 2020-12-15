inputFile = open("Day10testdata", "r")
inputData = inputFile.readlines()
strippedInputData = [int(x[:-1]) for x in inputData]
inputData = strippedInputData
inputData.sort()

print(inputData)

adaptorsToTest = [len(inputData)]
testedAdaptors = []

knownPaths = {}


def findallpaths(node, dataList):
    count = 0
    print(node)
    if node == 2:
        count = 2
    elif node < 2:
        count = 1
    else:
        for originIndex in range(3):
            if dataList[node] - dataList[node-originIndex-1] < 4 :
                if node in knownPaths:
                    count = count + knownPaths[node]
                else:
                    count = count + findallpaths(node-originIndex-1, dataList)
    knownPaths.update({node : count})
    return count

print(findallpaths(len(inputData)-1, inputData))

