def longestCommonSubsequence(str1, str2):
    if len(str2)> len(str1):
        (str1,str2) = (str2,str1)
    sequence = ''
   
    tempStr2 = str2[0:]

    lengthOftempStr2 = len(tempStr2)
    tempStr1 = str1

    for idx in range(len(str1)):
        tempStr1 = str1
        if idx > 0:
            tempStr1 = tempStr1[0:idx] + tempStr1[idx+1:]
        tempStr2 = str2[0:]
        lengthOftempStr2 = len(tempStr2)
        tempSequence = ''
        for item in tempStr1:
            if item in tempStr2:
                tempSequence += item
                index = tempStr2.index(item)
                if index == lengthOftempStr2 - 1:
                    break
                tempStr2 = tempStr2[index+1:]
                lengthOftempStr2 = len(tempStr2)
        
        if len(tempSequence) > len(sequence):
            sequence = tempSequence

    
    return [char for char in sequence]


# str11 = 'ZXVVYZW'
# str21 = 'XKYKZPW'

# str111 = "AB(CDEF)GHIJKLMNOPQRSTUVWXYZ",
# str211  = "(C)CC(D)D(E)GDHAGKGLWAJWKJAWGKGWJAKLGGWA(F)WLFFWA(GJ)W(K)AG"
# #["C", "D", "E", "F", "G", "J", "K"]

# str1 = "AB (CDE) F(G)(H)I(JKL)MNOPQRSTUV(W)XYZ",
# str2 = "(C)CC(D)D(E) (G)D(H)AGKGLWA(J)WKJAWG(K)GWJAK(L)GG(W)AWLFFWAGJWKAG"

#["C", "D", "E", "G", "H", "J", "K", "L", "W"]

str1 = 'abcdegh'
str2 = 'acdebe'

print(longestCommonSubsequence(str1,str2))