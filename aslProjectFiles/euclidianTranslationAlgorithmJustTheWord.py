from scipy.spatial import distance


helloAverageArray =  [1.063537209088, 1.259212335374, 1.187664706154, 2.999976190476, 3.0029529929159997, -28.7353657973, 28.978824204779993, 0.8]
deafAverageArray = [1.277544964828, 1.266982885854, 0.6441859197096, 2.94, 2.9402336631140003, -50.135392486659995, 16.69457222256, 0.6]
sillyAverageArray = [1.396204772702, 0.6883036504112001, 1.1958510765800001, 2.949943661972, 2.95076933502, -58.3648303067, 7.209095979839999, 0.85]
DontAverageArray = [1.43669847672, 0.6795903427953333, 0.6623329903721666, 2.940634022618333, 2.950024509803333, -55.73188094425, 11.517020842883333, 0.2]
sorryAverageArray = [1.2779846620459998, 0.6672442764404, 0.6671793404216, 2.94, 2.949325301204, -24.3464770199, 23.251798345799997, 0.4]
funnyAverageArray = [1.4767921885125, 1.2552810009375, 0.8077903494965, 2.9401521164024995, 3.0, -47.2233988709, 23.78069286775, 0.8]
veryFunnyAverageArray = [1.3210714210320835, 1.2192209640424996, 0.8349562954005414, 2.9641878926125003, 2.999870071684583, -59.79080522557084, 5.043013768885834, 0.9]
fineAverageArray = [1.4490565660633334, 1.248344099045, 0.9566220411433334, 2.990185411296667, 3.0000915750916666, -38.09338127386667, 25.853750872333336, 0.6]
hearingAverageArray = [1.335595713756, 1.2546168785440002, 0.6460207651392, 2.94, 2.9401419121659997, -6.631944609646, 47.27772743088, 0.6]
sameAverageArray = [1.4580320300760001, 0.6457537935558, 1.216785597538, 2.9429730186220002, 2.950114205344, -11.819801261806, 52.663371827679995, 0.6]
arrayOrder = ["flexBend1Averages", "flexBend2Averages", "flexBend3Averages", "flexBend4Averages", "flexBend5Averages", "pitchAverages", "rollAverages", "yawAverages", "accelXAverages", "accelYAverages", "accelZAverages"]
allWordArrays = [helloAverageArray, deafAverageArray, sillyAverageArray, DontAverageArray, sorryAverageArray, funnyAverageArray, veryFunnyAverageArray, fineAverageArray, hearingAverageArray, sameAverageArray]

def normalize(value, minimum, maximum):
    
    numerator = value - minimum
    denominator = maximum - minimum
    finalNormalizedValue = numerator/denominator
    
    return finalNormalizedValue

for array in allWordArrays:
    array[0] = normalize(array[0], 1.063537209088, 1.4767921885125)
    array[1] = normalize(array[1], 0.6457537935558, 1.266982885854)
    
    array[2] = normalize(array[2],  0.6441859197096, 1.216785597538)
    
    array[3] = normalize(array[3], 2.94, 2.999976190476)
    
    array[4] = normalize(array[4], 2.9401419121659997, 3.0029529929159997)
    
    array[5] = normalize(array[5], -59.79080522557084, -6.631944609646)
    
    array[6] = normalize(array[6], 5.043013768885834, 52.663371827679995)
    
    for i in array:
        print(i)


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



elementCounter = 0
badArrays = []

for element in splitData:
    if len(element) != 11:
        badArrays.append(elementCounter)
    elementCounter = elementCounter + 1
 

 
for badArray in badArrays:
    element = splitData[badArray]
    splitData.remove(element)
    counter = 0
    for badArray in badArrays:
        badArrays[counter] = badArray - 1
        counter = counter + 1




counter4 = 0

for array in splitData:
    counter4 = counter4 + 1
    rollAngles.append(array[0])
    pitchAngles.append(array[1])
    yawAngles.append(array[2])
    accelXs.append(array[3])
    
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
averagesArrayUnkownWord.append(pitchAverage)
averagesArrayUnkownWord.append(rollAverage)


averagesArrayUnkownWord[0] = normalize(averagesArrayUnkownWord[0], 1.063537209088, 1.4767921885125)
averagesArrayUnkownWord[1] = normalize(averagesArrayUnkownWord[1],0.6457537935558, 1.266982885854)
averagesArrayUnkownWord[2] = normalize(averagesArrayUnkownWord[2], 0.6441859197096, 1.216785597538)
averagesArrayUnkownWord[3] = normalize(averagesArrayUnkownWord[3], 2.94, 2.999976190476)
averagesArrayUnkownWord[4] = normalize(averagesArrayUnkownWord[4], 2.9401419121659997, 3.0029529929159997)
averagesArrayUnkownWord[5] = normalize(averagesArrayUnkownWord[5], -59.79080522557084, -6.631944609646)
averagesArrayUnkownWord[6] = normalize(averagesArrayUnkownWord[6], 5.043013768885834, 52.663371827679995)



leastDistanceArray = []
euclidianDistance = 10000
counter = 0
leastDistanceArrayNumber = 0


for array in allWordArrays:
    euclidianDistance = distance.euclidean(averagesArrayUnkownWord, array[0:7])
    if counter == 0:
        with open("./helloEuclidianDistances.txt", "a") as hello:
            hello.write(str(euclidianDistance)+ "\n")
    if counter == 1:
        with open("./deafEuclidianDistances.txt", "a") as deaf:
            deaf.write(str(euclidianDistance)+ "\n")
    if counter == 2:
        with open("./sillyEuclidianDistances.txt", "a") as silly:
            silly.write(str(euclidianDistance)+ "\n")
    if counter == 3:
        with open("./dontEuclidianDistances.txt", "a") as dont:
            dont.write(str(euclidianDistance)+ "\n")
    if counter == 4:
        with open("./sorryEuclidianDistances.txt", "a") as sorry:
            sorry.write(str(euclidianDistance)+ "\n")
    if counter == 5:
        with open("./funnyEuclidianDistances.txt", "a") as funny:
            funny.write(str(euclidianDistance)+ "\n")
    if counter == 6:
        with open("./veryfunnyEuclidianDistances.txt", "a") as veryfunny:
            veryfunny.write(str(euclidianDistance)+ "\n")
    if counter == 7:
        with open("./fineEuclidianDistances.txt", "a") as fine:
            fine.write(str(euclidianDistance)+ "\n")
    if counter == 8:
        with open("./hearingEuclidianDistances.txt", "a") as hearing:
            hearing.write(str(euclidianDistance)+ "\n")
    if counter == 9:
        with open("./sameEuclidianDistances.txt", "a") as same:
            same.write(str(euclidianDistance) + "\n")
    counter = counter + 1



counter = 0
for array in allWordArrays:

    if  distance.euclidean(averagesArrayUnkownWord, array[0:7]) < euclidianDistance :
        euclidianDistance = distance.euclidean(averagesArrayUnkownWord, array[0:7])
        

        leastDistanceArray = array
        leastDistanceArrayNumber = counter
    counter = counter + 1


finalWordTranslation = allWords[leastDistanceArrayNumber]
print(str(finalWordTranslation))

#findAverage(valuesArray)









