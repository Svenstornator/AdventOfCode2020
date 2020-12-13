inputFile = open("Day2Input", "r")
inputData = inputFile.readlines()
strippedInputData = [x[:-1] for x in inputData]
inputData = strippedInputData

passwordMinimum = []
passwordMaximum = []
passwordCharacter = []
passwords = []
invalids = 0

for data in inputData:
    entry = data.split(":")
    passwordRule = entry[0].split("-")
    passwordMinimum.append(passwordRule[0])
    passwordMaximum.append(passwordRule[1].split(" ")[0])
    passwordCharacter.append(passwordRule[1].split()[1])
    passwords.append(entry[1])


for i in range(len(passwords)):
    count = 0
    password = passwords[i]
    for character in password:
        if character == passwordCharacter[i]:
            count = count+1
    if count > int(passwordMaximum[i]) or count < int(passwordMinimum[i]):
        invalids = invalids + 1

print(invalids)