inputFile = open("Day6Input", "r")
inputData = inputFile.read().split('\n\n')

count = 0

for group in inputData:
    individualResponses = []
    numberInGroup = len(group.split('\n'))
    group = group.replace("\n","")
    for character in group:
        if group.count(character) == numberInGroup:
            individualResponses.append(character)
    count = count + len(set(individualResponses))

print(count)
