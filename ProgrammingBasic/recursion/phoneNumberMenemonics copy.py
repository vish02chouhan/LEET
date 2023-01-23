def phoneNumberMnemonics(phoneNumber):
    result = []
    helper('',phoneNumber, mnemonics,result)
    print(result)
    return result

def helper(current, phoneNumber, mnemonics, result):
    if len(phoneNumber) == 0:
        result.append(current)
        return

    #for num in phoneNumber:
    chars = mnemonics[phoneNumber[0]]
    for char in chars:
        newPhoneNumber = phoneNumber[1:]
        helper(current + char, newPhoneNumber, mnemonics, result)
            
        

mnemonics = {
'0': ['0'],
'1': ['1'],
'2': ['a','b','c'],
'3': ['d','e','f'],
'4': ['g','h','i'],
'5': ['j','k','l'],
'6': ['m','n','o'],
'7': ['p','q','r','s'],
'8': ['t','u','v'],
'9': ['w','x','y', 'z']

}

phoneNumberMnemonics('1905')