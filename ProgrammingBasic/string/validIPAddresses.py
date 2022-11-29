def validIPAddresses(string):
    validParts = {}
    getLastPart(string, validParts,3)


    for index in range(3,1,-1):
        subString = ''
        for item in validParts[index]:
            print(item)
            subString = string[:len(string)-len(item)]
            getLastPart(subString, validParts,index-1)
        
        string = string[:len(string)- len(subString)]
    
    print(validParts)


def getLastPart(string, validParts, part):
    for item in reversed(range(len(string))):
        if validPart(string[item:]):
            validParts[part] = {}
        else:
            return string[:len(string) - len(validParts[part][-1])]
            
    

def validPart(substring):
    if len(substring) > 1 and substring[0] == '0':
        return False
    ipPart = float(substring)

    return True if ipPart >= 0 and ipPart <= 255 else False


print(validIPAddresses('1921680'))

