inputFile = open("Day7Input", "r")
inputData = inputFile.read().split('\n')

bagRules = {}
bagsToFind = ["shiny gold"]

# Extract information into a useable format
for rule in inputData:
    ruleWords = rule.split(' ')
    ruleList = {}
    for word in range(3,len(ruleWords)):
        ruleWords[word] = ruleWords[word].replace(',', "")
        ruleWords[word] = ruleWords[word].replace('.', "")
        if ruleWords[word] == "bag" or ruleWords[word] == "bags":
            ruleList.update({ruleWords[word-2] + " " + ruleWords[word-1] : ruleWords[word-3] })
    bagRules.update({ruleWords[0] + " " + ruleWords[1] : ruleList})

print(bagRules)

def containsbags(bag, allBags):
    count = 0
    containedBags = allBags[bag]
    for individualBag in containedBags:
        if not individualBag == 'no other':
            count = count + int(containedBags[individualBag]) * (1 + containsbags(individualBag, allBags))
    return count

print(containsbags("shiny gold", bagRules))