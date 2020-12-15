inputFile = open("Day8Input", "r")
inputData = inputFile.readlines()
strippedInputData = [x[:-1] for x in inputData]
inputData = strippedInputData

command = []
value = []
endCondition = True

for data in inputData:
    data = data.split(" ")
    command.append(data[0])
    value.append(data[1])


index = 0
executedIndices = []
count = 0
while(endCondition):
    if index in executedIndices:
        print(count)
        break
    else:
        executedIndices.append(index)
    if command[index] == 'acc':
        if value[index][0] == '+':
            count = count + int(value[index][1:])
        elif value[index][0] == '-':
            count = count - int(value[index][1:])
        index = index + 1
    elif command[index] == 'jmp':
        if value[index][0] == '+':
            index = index + int(value[index][1:])
        elif value[index][0] == '-':
            index = index - int(value[index][1:])
    elif command[index] == 'nop':
        executedIndices.append(index)
        index = index + 1