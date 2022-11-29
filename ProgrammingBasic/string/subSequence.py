


def isSubstringExists(mainString, subString):

    subStringPointer = 0
    mainStringPointer = 0



    while subStringPointer < len(subString)  and mainStringPointer < len(mainString):

            if mainString[mainStringPointer] != subString[subStringPointer]:
                mainStringPointer += 1
            else:
                mainStringPointer +=1
                subStringPointer +=1



    
    if mainStringPointer >= len(mainString) and subStringPointer < len(subString):
        return False
    
    return True

mainString = 'babzab'
subString = 'abc'

print(isSubstringExists(mainString,subString))


    


