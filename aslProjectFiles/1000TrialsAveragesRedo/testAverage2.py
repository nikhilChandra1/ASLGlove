# coding=utf-8

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '=', '~']
file = open("../test.txt", "r")
data = []
for line in file:
        data.append(line)

counter = 0

for i in data:
    if i.endswith('\r\n'):
        data[counter] = i[:-2]
    if i.endswith('\r'):
        data[counter] = i[:-1]
    counter = counter + 1

while("" in data) :
    data.remove("")

counter = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53]

editedData = []
counter2 = 0
for i in data:
    for j in letters:
        if j not in i:
            counter2 = counter2 + 1
    if counter2 == 54:
        editedData.append(i)
    counter2 = 0
            

splitData = []

for string in editedData:
    splitData.append(string.split("/"))
    

rollAngles = []
pitchAngles = []
yawAngles = []
accelXs = []
accelYs = []
accelZs = []
flexBend1s = []
flexBend2s = []
flexBend3s = []
flexBend4s = []
flexBend5s = []

del splitData[-1]
del splitData[0]
print(splitData)


elementCounter = 0
badArrays = []

for element in splitData:
    if len(element) != 11:
        badArrays.append(elementCounter)
    elementCounter = elementCounter + 1
 
print(badArrays)
 
for badArray in badArrays:
    element = splitData[badArray]
    splitData.remove(element)
    counter = 0
    for badArray in badArrays:
        badArrays[counter] = badArray - 1
        counter = counter + 1

print(splitData)





counter4 = 0

for array in splitData:
    print(array)
    counter4 = counter4 + 1
    rollAngles.append(array[0])
    pitchAngles.append(array[1])
    yawAngles.append(array[2])
    accelXs.append(array[3])
    print(counter4)
    accelYs.append(array[4])
    accelZs.append(array[5])
    flexBend1s.append(array[6])
    flexBend2s.append(array[7])
    flexBend3s.append(array[8])
    flexBend4s.append(array[9])
    flexBend5s.append(array[10])
    


def findAverage(array):
    sum = 0.0
    for value in array:
        sum = sum + float(value)
    numberOfElements = len(array)
    average = sum/numberOfElements
    
    return  average

rollAverage = findAverage(rollAngles)
pitchAverage = findAverage(pitchAngles)
yawAverage = findAverage(yawAngles)
accelXAverage = findAverage(accelXs)
accelYAverage = findAverage(accelYs)
accelZAverage = findAverage(accelZs)
flexBend1Average = findAverage(flexBend1s)
flexBend2Average = findAverage(flexBend2s)
flexBend3Average = findAverage(flexBend3s)
flexBend4Average = findAverage(flexBend4s)
flexBend5Average = findAverage(flexBend5s)

def appendAverageToFile(value, file):
    File = open(file, "a")
    File.write(str(value))
    File.write("\n")
    File.close()
    


appendAverageToFile(rollAverage, "rollAverages8.txt")
appendAverageToFile(pitchAverage, "pitchAverages8.txt")
appendAverageToFile(yawAverage, "yawAverages8.txt")
appendAverageToFile(accelXAverage, "accelXAverages8.txt")
appendAverageToFile(accelYAverage, "accelYAverages8.txt")
appendAverageToFile(accelZAverage, "accelZAverages8.txt")
appendAverageToFile(flexBend1Average, "flexBend1Averages8.txt")
appendAverageToFile(flexBend2Average, "flexBend2Averages8.txt")
appendAverageToFile(flexBend3Average, "flexBend3Averages8.txt")
appendAverageToFile(flexBend4Average, "flexBend4Averages8.txt")
appendAverageToFile(flexBend5Average, "flexBend5Averages8.txt")






#next crreate six different files, for each append the average each time
