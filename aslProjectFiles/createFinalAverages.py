def getFinalAverage(File):

    averageFile = open(File, "r")
    averages = []
    counter = 0
    sum = 0.0
    for line in averageFile:
        averages.append(line)
        counter = counter + 1
    for value in averages:
        try:
            sum = sum + float(value)
        except:
            pass
    average = sum/counter
    
    return average
    

def getArrayBasedOnFileNumber(fileNumber):
    fileTypeArray = ["flexBend1Averages", "flexBend2Averages", "flexBend3Averages", "flexBend4Averages", "flexBend5Averages", "pitchAverages", "rollAverages"]
    allWords = ["hello", "deaf", "silly", "Dont", "sorry", "funny", "fine", "hearing", "same"]
    averageArray = []
    wordNumber = 0
    if fileNumber == "":
        wordNumber = 0
    else:
        wordNumber = int(fileNumber)
        
    averageArray.append(allWords[wordNumber])
    
    for fileType in fileTypeArray:
        averageArray.append(getFinalAverage(fileType + fileNumber + ".txt"))
        
    return averageArray

print(getArrayBasedOnFileNumber(""))
print(getArrayBasedOnFileNumber("1"))
print(getArrayBasedOnFileNumber("2"))
print(getArrayBasedOnFileNumber("3"))
print(getArrayBasedOnFileNumber("4"))
print(getArrayBasedOnFileNumber("5"))
print(getArrayBasedOnFileNumber("6"))
print(getArrayBasedOnFileNumber("7"))
print(getArrayBasedOnFileNumber("8"))


    
    
    

