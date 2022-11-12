def longestCommonSubsequence1(str1, str2):    
    small = str1 if len(str1) < len(str2) else str2    
    big = str1 if len(str1) >= len(str2) else str2    
    evenLcs = [[] for x in range(len(small) + 1)]    
    oddLcs = [[] for x in range(len(small) + 1)]    
    for i in range(1, len(big) + 1):        
        if i % 2 == 1:            
            currentLcs = oddLcs            
            previousLcs = evenLcs        
        else:            
            currentLcs = evenLcs            
            previousLcs = oddLcs        
        for j in range(1, len(small) + 1):            
            if big[i - 1] == small[j - 1]:                
                currentLcs[j] = previousLcs[j - 1] + [big[i - 1]]            
            else:                
                currentLcs[j] = max(previousLcs[j], currentLcs[j - 1], key=len) 

    print(evenLcs)   
    print(oddLcs)
    return evenLcs[-1] if len(big) % 2 == 0 else oddLcs[-1]

str1  = "ZXVVYZW"
str2  = "XKYKZPW"


str11 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str22  = "CCCDDEGDHAGKGLWAJWKJAWGKGWJAKLGGWAFWLFFWAGJWKAG"




print(longestCommonSubsequence1(str1,str2))