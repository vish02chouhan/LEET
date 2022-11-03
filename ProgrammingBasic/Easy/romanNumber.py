# romanAlphabet = ['I','V','X','L','C','D','M']

# def converttoRoman():
#     pass
print('test')

symbolDict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

romanstring = 'MCMXCIV'
groupArray = []
skipIndex = -1

for index, item in enumerate(romanstring):
    print(index, item)

for index, item in enumerate(romanstring):

    if index == skipIndex:
        skipIndex = -1
        continue


    

    if symbolDict[romanstring[index+1]] > symbolDict[romanstring[index]]:
        groupArray.append((symbolDict[romanstring[index+1]] - symbolDict[romanstring[index]]))
        skipIndex = index + 1
    else:
        groupArray.append(symbolDict[item])


totalSum = 0
for item in groupArray:
    totalSum += item

print(totalSum)