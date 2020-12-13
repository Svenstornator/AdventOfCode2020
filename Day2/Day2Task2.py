inputFile = open("Day2Input", "r")
inputData = inputFile.readlines()
strippedInputData = [x[:-1] for x in inputData]
inputData = strippedInputData

passwordPosition1 = []
passwordPosition2 = []
passwordCharacter = []
passwords = []
valids = 0

for data in inputData:
    entry = data.split(":")
    passwordRule = entry[0].split("-")
    passwordPosition1.append(int(passwordRule[0])-1)
    passwordPosition2.append(int(passwordRule[1].split(" ")[0])-1)
    passwordCharacter.append(passwordRule[1].split()[1])
    passwords.append(entry[1][1:])


for i in range(len(passwords)):
    count = 0
    password = passwords[i]
    if password[passwordPosition1[i]]==passwordCharacter[i]:
        count = count+1
    if password[passwordPosition2[i]]==passwordCharacter[i]:
        count = count+1
    if count == 1:
        valids = valids + 1

print(valids)