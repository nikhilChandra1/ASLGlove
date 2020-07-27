

stopArray = [100, 199,  300, 431, 535, 637, 751, 853, 968]

hello = 0.8
deaf = 0.6
silly = 0.85
dont = 0.2
sorry = 0.4
funny = 0.8
veryFunny = 0.9
fine = 0.6
hearing = 0.6
same = 0.6


def oneTextFileEdit(startFile, ammendedFile, facialExpression, stopPoint, expectedFacialExpression):
    file = open(startFile, "r")
    data = []
    for line in file:
            data.append(line)
    counter = 0
    file = open(ammendedFile, "a")
    previousPoint = stopArray[stopPoint - 1]
    if stopPoint == 0:
        previousPoint = 0
    for value in data:
        
        if counter >= previousPoint:
            newValue = float(value) + abs(expectedFacialExpression - facialExpression)
            file.write(str(newValue) + "\n")
        if counter == stopArray[stopPoint]:
            break
        counter = counter + 1
        
    file.close()





def createUpdatedTextFile(facialExpression, stopPoint):
    oneTextFileEdit("helloEuclidianDistances.txt", "helloEuclidianDistancesAmmended.txt", facialExpression, stopPoint, hello)
    oneTextFileEdit("deafEuclidianDistances.txt", "deafEuclidianDistancesAmmended.txt", facialExpression, stopPoint, deaf)
    oneTextFileEdit("sillyEuclidianDistances.txt", "sillyEuclidianDistancesAmmended.txt", facialExpression, stopPoint, silly)
    oneTextFileEdit("dontEuclidianDistances.txt", "dontEuclidianDistancesAmmended.txt", facialExpression, stopPoint, dont)
    oneTextFileEdit("sorryEuclidianDistances.txt", "sorryEuclidianDistancesAmmended.txt", facialExpression, stopPoint, sorry)
    oneTextFileEdit("funnyEuclidianDistances.txt", "funnyEuclidianDistancesAmmended.txt", facialExpression, stopPoint, funny)
    oneTextFileEdit("funnyEuclidianDistances.txt", "veryFunnyEuclidianDistancesAmmended.txt", facialExpression, stopPoint, veryFunny)
    oneTextFileEdit("fineEuclidianDistances.txt", "fineEuclidianDistancesAmmended.txt", facialExpression, stopPoint, fine)
    oneTextFileEdit("hearingEuclidianDistances.txt", "hearingEuclidianDistancesAmmended.txt", facialExpression, stopPoint, hearing)
    oneTextFileEdit("sameEuclidianDistances.txt", "sameEuclidianDistancesAmmended.txt", facialExpression, stopPoint, same)
    

createUpdatedTextFile(hello, 0)
createUpdatedTextFile(deaf, 1)
createUpdatedTextFile(silly, 2)
createUpdatedTextFile(dont, 3)
createUpdatedTextFile(sorry, 4)
createUpdatedTextFile(funny, 5)
createUpdatedTextFile(veryFunny, 5)
createUpdatedTextFile(fine, 6)
createUpdatedTextFile(hearing, 7)
createUpdatedTextFile(same, 8)

