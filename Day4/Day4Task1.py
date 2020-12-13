inputFile = open("Day4Input", "r")
inputData = inputFile.read()

separatedPassports = inputData.split('\n\n')
organizedPassports = []
valid = 0
validPassports = []

for passport in separatedPassports:
    passport = passport.replace("\n", " ")
    passportsWithSeparatedFields = passport.split(" ")
    passportDict = {}
    for field in passportsWithSeparatedFields:
        separatedField = field.split(":")
        passportDict.update({separatedField[0]:separatedField[1]})
    organizedPassports.append(passportDict)


for passport in organizedPassports:
    if len(passport) == 8:
        valid = valid + 1
        validPassports.append(passport)
    if len(passport) == 7:
        if "cid" not in passport.keys():
            valid = valid + 1
            validPassports.append(passport)

print(len(validPassports))