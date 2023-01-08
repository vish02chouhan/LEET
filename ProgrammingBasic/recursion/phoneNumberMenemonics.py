def phoneNumberMnemonics(phoneNumber):
    
    mnemonics = ['']

    #1905
    digitCharacterHash = {'0':'1','1':'1', '2':'abc', '3':'def', '4':'ghi', 
                          '5':'jkl', '6':'mon','7':'pqr', 
                          '8':'stuv', '9':'wxyz' }

    for digit in phoneNumber:
        currentCharacters = digitCharacterHash[digit]
        for char in currentCharacters:
            for i in range(len(mnemonics)):
                
                mnemonics[i] = mnemonics[i]+char


    return [item for item in mnemonics if len(item)==len(phoneNumber)]


print(phoneNumberMnemonics('1905'))