stopArray = [100, 199,  300, 431, 535, 637, 739, 851, 953, 1068]
stopAmmendedArray = [100, 199,  300, 431, 535, 637, 739, 841, 953, 1055, 1170]
file = open("helloEuclidianDistances.txt")
helloData = []
for line in file:
        helloData.append(line)


file = open("deafEuclidianDistances.txt")
deafData = []
for line in file:
        deafData.append(line)


file = open("sillyEuclidianDistances.txt")
sillyData = []
for line in file:
        sillyData.append(line)

file = open("dontEuclidianDistances.txt")
dontData = []
for line in file:
        dontData.append(line)

file = open("sorryEuclidianDistances.txt")
sorryData = []
for line in file:
        sorryData.append(line)

file = open("funnyEuclidianDistances.txt")
funnyData = []
for line in file:
        funnyData.append(line)

file = open("fineEuclidianDistances.txt")
fineData = []
for line in file:
        fineData.append(line)
        
file = open("hearingEuclidianDistances.txt")
hearingData = []
for line in file:
        hearingData.append(line)

file = open("sameEuclidianDistances.txt")
sameData = []
for line in file:
        sameData.append(line)

file = open("helloEuclidianDistancesAmmended.txt")
helloAmmendedData = []
for line in file:
        helloAmmendedData.append(line)


file = open("deafEuclidianDistancesAmmended.txt")
deafAmmendedData = []
for line in file:
        deafAmmendedData.append(line)


file = open("sillyEuclidianDistancesAmmended.txt")
sillyAmmendedData = []
for line in file:
        sillyAmmendedData.append(line)

file = open("dontEuclidianDistancesAmmended.txt")
dontAmmendedData = []
for line in file:
        dontAmmendedData.append(line)

file = open("sorryEuclidianDistancesAmmended.txt")
sorryAmmendedData = []
for line in file:
        sorryAmmendedData.append(line)

file = open("funnyEuclidianDistancesAmmended.txt")
funnyAmmendedData = []
for line in file:
        funnyAmmendedData.append(line)
        
file = open("veryFunnyEuclidianDistancesAmmended.txt")
veryFunnyAmmendedData = []
for line in file:
    veryFunnyAmmendedData.append(line)

file = open("fineEuclidianDistancesAmmended.txt")
fineAmmendedData = []
for line in file:
        fineAmmendedData.append(line)
        
file = open("hearingEuclidianDistancesAmmended.txt")
hearingAmmendedData = []
for line in file:
        hearingAmmendedData.append(line)

file = open("sameEuclidianDistancesAmmended.txt")
sameAmmendedData = []
for line in file:
        sameAmmendedData.append(line)

counter = 0
highestEuclidianDistance = 0
smallestEuclidianDistance = 100000

def findEuclidianDistances(array, stop):
    global highestEuclidianDistance
    global smallestEuclidianDistance
    euclidianDistances = []
    counter = stopArray[stop - 1]
    if stop == 0:
        counter = 0
    
    while counter <= stopArray[stop]:
        firstValue = float(array[counter])
        secondValue = (float(deafData[counter]) + float(sillyData[counter]) + float(dontData[counter]) + float(sorryData[counter]) + float(funnyData[counter]) + float(fineData[counter]) + float(hearingData[counter]) + float(sameData[counter]) + float(helloData[counter]) - firstValue)/8.0
        euclidianDistance = firstValue - secondValue
        euclidianDistances.append(euclidianDistance)
        counter = counter + 1
        if euclidianDistance > highestEuclidianDistance:
            highestEuclidianDistance = euclidianDistance
        if euclidianDistance < smallestEuclidianDistance and euclidianDistance >= 0 :
            smallestEuclidianDistance = euclidianDistance
    return euclidianDistances
    



def findEuclidianDistancesAmmended(array, stop):
    global highestEuclidianDistance
    global smallestEuclidianDistance
    euclidianDistances = []
    counter = stopAmmendedArray[stop - 1]
    if stop == 0:
        counter = 0
    
    while counter <= stopAmmendedArray[stop]:
        
        firstValue = float(array[counter])
        secondValue = (float(deafAmmendedData[counter]) + float(sillyAmmendedData[counter]) + float(dontAmmendedData[counter]) + float(sorryAmmendedData[counter]) + float(funnyAmmendedData[counter]) + float(fineAmmendedData[counter]) + float(hearingAmmendedData[counter]) + float(sameAmmendedData[counter]) + float(helloAmmendedData[counter]) + float(veryFunnyAmmendedData[counter]) - firstValue)/9.0
        euclidianDistance = secondValue - firstValue
        euclidianDistances.append(euclidianDistance)
        counter = counter + 1
        if euclidianDistance > highestEuclidianDistance:
            highestEuclidianDistance = euclidianDistance
        if euclidianDistance < smallestEuclidianDistance and euclidianDistance >= 0 :
                smallestEuclidianDistance = euclidianDistance
    
    return euclidianDistances
    

helloEuclidianDistances = findEuclidianDistances(helloData, 0)
deafEuclidianDistances = findEuclidianDistances(deafData, 1)
sillyEuclidianDistances = findEuclidianDistances(sillyData, 2)
dontEuclidianDistances = findEuclidianDistances(dontData, 3)
sorryEuclidianDistances = findEuclidianDistances(sorryData, 4)
funnyEuclidianDistances = findEuclidianDistances(funnyData, 5)
fineEuclidianDistances = findEuclidianDistances(fineData, 6)
hearingEuclidianDistances = findEuclidianDistances(hearingData, 7)
sameEuclidianDistances = findEuclidianDistances(sameData, 8)

helloAmmendedEuclidianDistances = findEuclidianDistancesAmmended(helloAmmendedData, 0)
deafAmmendedEuclidianDistances = findEuclidianDistancesAmmended(deafAmmendedData, 1)
sillyAmmendedEuclidianDistances = findEuclidianDistancesAmmended(sillyAmmendedData, 2)
dontAmmendedEuclidianDistances = findEuclidianDistancesAmmended(dontAmmendedData, 3)
sorryAmmendedEuclidianDistances = findEuclidianDistancesAmmended(sorryAmmendedData, 4)
funnyAmmendedEuclidianDistances = findEuclidianDistancesAmmended(funnyAmmendedData, 5)
veryFunnyAmmendedEuclidianDistances = findEuclidianDistancesAmmended(veryFunnyAmmendedData, 6)
fineAmmendedEuclidianDistances = findEuclidianDistancesAmmended(fineAmmendedData, 7)
hearingAmmendedEuclidianDistances = findEuclidianDistancesAmmended(hearingAmmendedData, 8)
sameAmmendedEuclidianDistances = findEuclidianDistancesAmmended(sameAmmendedData, 9)


print(highestEuclidianDistance)
print(smallestEuclidianDistance)

def createConfidenceFile(fileWord, array):
    counter = 0
    file = open((fileWord + "Confidences.txt"), "w")
    for value in array:
        numerator = float(value)
        denominator = highestEuclidianDistance - smallestEuclidianDistance
        confidence = abs(numerator/denominator)
        file.write(str(confidence) + "\n")
        counter = counter + 1
        if counter == 1:
            file.close()
            file = open((fileWord + "Confidences.txt"), "a")
    file.close()
        
createConfidenceFile("hello", helloEuclidianDistances)
createConfidenceFile("deaf", deafEuclidianDistances)
createConfidenceFile("silly", sillyEuclidianDistances)
createConfidenceFile("dont", dontEuclidianDistances)
createConfidenceFile("sorry", sorryEuclidianDistances)
createConfidenceFile("hello", helloEuclidianDistances)
createConfidenceFile("funny", helloEuclidianDistances)
createConfidenceFile("fine", fineEuclidianDistances)
createConfidenceFile("hearing", hearingEuclidianDistances)
createConfidenceFile("same", sameEuclidianDistances)


createConfidenceFile("deafAmmended", deafAmmendedEuclidianDistances)
createConfidenceFile("sillyAmmended", sillyAmmendedEuclidianDistances)
createConfidenceFile("dontAmmended", dontAmmendedEuclidianDistances)
createConfidenceFile("sorryAmmended", sorryAmmendedEuclidianDistances)
createConfidenceFile("helloAmmended", helloAmmendedEuclidianDistances)
createConfidenceFile("funnyAmmended", helloAmmendedEuclidianDistances)
createConfidenceFile("veryFunnyAmmended", helloAmmendedEuclidianDistances)
createConfidenceFile("fineAmmended", fineAmmendedEuclidianDistances)
createConfidenceFile("hearingAmmended", hearingAmmendedEuclidianDistances)
createConfidenceFile("sameAmmended", sameAmmendedEuclidianDistances)
        







