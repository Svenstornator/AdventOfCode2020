inputFile = open("Day6Input", "r")
inputData = inputFile.read().split('\n\n')

count = 0

for group in inputData:
    individualResponses = []
    group = group.replace("\n","")
    for character in group:
        individualResponses.append(character)
    count = count + len(set(group))

print(count)

