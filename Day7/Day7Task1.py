inputFile = open("Day7Input", "r")
inputData = inputFile.read().split('\n')

nominativeBag = []
accusativeBags = []
bagsToFind = ["shiny gold"]
possibleBags = []

# Extract information into a useable format
for rule in inputData:
    ruleWords = rule.split(' ')
    nominativeBag.append(ruleWords[0] + " " + ruleWords[1])
    ruleList = []
    for word in range(3,len(ruleWords)):
        ruleWords[word] = ruleWords[word].replace(',', "")
        ruleWords[word] = ruleWords[word].replace('.', "")
        if ruleWords[word] == "bag" or ruleWords[word] == "bags":
            ruleList.append(ruleWords[word-2] + " " + ruleWords[word-1])
    accusativeBags.append(ruleList)

while not len(bagsToFind) == 0:
    findingBag = bagsToFind.pop(0)
    if findingBag not in possibleBags:
        possibleBags.append(findingBag)
    for index in range(len(accusativeBags)):
        if findingBag in accusativeBags[index]:
            bagsToFind.append(nominativeBag[index])

#Subtract one for length because shiny bag cannot contain itself
print(len(possibleBags)-1)
