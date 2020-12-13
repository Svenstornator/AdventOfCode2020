import re
hair = re.compile("#[0-9a-f]{6}$")
pid = re.compile("[0-9]{9}$")

inputFile = open("Day4Input", "r")
inputData = inputFile.read()

separatedPassports = inputData.split('\n\n')
organizedPassports = []
validPassports = []
finalPassports = []

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
        validPassports.append(passport)
    if len(passport) == 7:
        if "cid" not in passport.keys():
            validPassports.append(passport)


for passport in validPassports:
    if not 1920 <= int(passport.get("byr")) <= 2002:
        continue
    if not 2010 <= int(passport.get("iyr")) <= 2020:
        continue
    if not 2020 <= int(passport.get("eyr")) <= 2030:
        continue
    if not passport.get("hgt")[-2:] == "cm" and not passport.get("hgt")[-2:] == "in":
        continue
    if passport.get("hgt")[-2:] == "cm":
        if not 150 <= int(passport.get("hgt")[:-2]) <= 193:
            continue
    if passport.get("hgt")[-2:] == "in":
        if not 59 <= int(passport.get("hgt")[:-2]) <= 76:
            continue
    if not passport.get("ecl") in ["amb","blu","brn","gry","grn","hzl","oth"]:
        continue
    if not hair.search(passport.get("hcl")):
        continue
    if not pid.match(passport.get("pid")):
        continue
    finalPassports.append(passport)

print(len(finalPassports))


