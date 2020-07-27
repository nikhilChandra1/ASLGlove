from scipy.spatial import distance

helloAverageArray =  [1.2064061923887097, 1.2494081537825807, 1.2231220089229031, 3.006950774898386, 3.0027944413003227, 0.8]
deafAverageArray = [1.250882928934348, 1.2194706467952177, 0.9172525968539564, 2.96, 2.9551133145926087, 0.6]
sillyAverageArray = [1.4795473334486116, 0.9111813265994445, 1.2073349740936112, 2.9778140050008326, 2.9697019952399994, 0.85]
DontAverageArray = [1.2485517546994285, 1.099503607468, 0.7550763969156857, 2.953213548316, 2.8841857832071434, 0.2]
sorryAverageArray = [1.2595426812762067, 0.7385978418074483, 0.7225163015627586, 2.950226636564483, 2.9499691846920695, 0.4]
funnyAverageArray = [1.3210714210320835, 1.2192209640424996, 0.8349562954005414, 2.9641878926125003, 2.999870071684583, 0.8]
veryFunnyAverageArray = [1.3210714210320835, 1.2192209640424996, 0.8349562954005414, 2.9641878926125003, 2.999870071684583, 0.9]
fineAverageArray = [1.6281720612264103, 1.2197799356466668, 1.199040429251282, 3.010056966814873, 3.000409666627179, 0.6]
hearingAverageArray = [1.2392315016905882, 1.209956218461176, 0.6930589950833824, 2.9499480075900015, 2.949441080167647, 0.6]
sameAverageArray = [1.3796365329385292, 0.7429468021721471, 1.0730263631691175, 2.9581034829426467, 2.962304654028234, 0.6]

arrayOrder = ["flexBend1Averages", "flexBend2Averages", "flexBend3Averages", "flexBend4Averages", "flexBend5Averages", "pitchAverages", "rollAverages", "yawAverages", "accelXAverages", "accelYAverages", "accelZAverages"]
allWordArrays = [helloAverageArray, deafAverageArray, sillyAverageArray, DontAverageArray, sorryAverageArray, funnyAverageArray, veryFunnyAverageArray, fineAverageArray, hearingAverageArray, sameAverageArray]

def normalize(value, minimum, maximum):
    
    numerator = value - minimum
    denominator = maximum - minimum
    finalNormalizedValue = numerator/denominator
    
    return finalNormalizedValue

for array in allWordArrays:
    array[0] = normalize(array[0], 1.2064061923887097, 1.6281720612264103)
    array[1] = normalize(array[1], 0.7385978418074483, 1.2494081537825807)
    array[2] = normalize(array[2], 0.6930589950833824, 1.2231220089229031)
    array[3] = normalize(array[3], 2.9499480075900015, 3.010056966814873)
    array[4] = normalize(array[4], 2.949441080167647, 3.0027944413003227)
    


allWords = ["Hello", "Deaf", "Silly", "Don't", "Sorry", "Funny", "Very Funny", "Fine", "Hearing", "Same"]

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '=', '~']
file = open("test.txt", "r")
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

arrayOrder = ["flexBend1Averages", "flexBend2Averages", "flexBend3Averages", "flexBend4Averages", "flexBend5Averages", "pitchAverages", "rollAverages", "yawAverages", "accelXAverages", "accelYAverages", "accelZAverages"]

averagesArrayUnkownWord = []
averagesArrayUnkownWord.append(flexBend1Average)
averagesArrayUnkownWord.append(flexBend2Average)
averagesArrayUnkownWord.append(flexBend3Average)
averagesArrayUnkownWord.append(flexBend4Average)
averagesArrayUnkownWord.append(flexBend5Average)


facialExpressionNumber = input("Facial Expression: ")
averagesArrayUnkownWord.append(float(facialExpressionNumber))


averagesArrayUnkownWord[0] = normalize(averagesArrayUnkownWord[0], 1.2064061923887097, 1.6281720612264103)
averagesArrayUnkownWord[1] = normalize(averagesArrayUnkownWord[1], 0.7385978418074483, 1.2494081537825807)
averagesArrayUnkownWord[2] = normalize(averagesArrayUnkownWord[2], 0.6930589950833824, 1.2231220089229031)
averagesArrayUnkownWord[3] = normalize(averagesArrayUnkownWord[3], 2.9499480075900015, 3.010056966814873)
averagesArrayUnkownWord[4] = normalize(averagesArrayUnkownWord[4], 2.949441080167647, 3.0027944413003227)


print(averagesArrayUnkownWord)

leastDistanceArray = []
euclidianDistance = 10000
counter = 0
leastDistanceArrayNumber = 0
for array in allWordArrays:
    print(distance.euclidean(averagesArrayUnkownWord, array[0:6]))
    if  distance.euclidean(averagesArrayUnkownWord, array[0:6]) < euclidianDistance :
        euclidianDistance = distance.euclidean(averagesArrayUnkownWord, array[0:6])
        leastDistanceArray = array
        leastDistanceArrayNumber = counter
    counter = counter + 1


finalWordTranslation = allWords[leastDistanceArrayNumber]
print("Final Word: " + str(finalWordTranslation))

#findAverage(valuesArray)
