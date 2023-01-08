def romanToInt(s: str) -> int:
    romanHash:map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    sum:int = 0
    startIndex:int = 0



    while startIndex < len(s):
        currentCharacter:str = s[startIndex]
        currentRomanInt:str =  romanHash[currentCharacter]
        nextRomanInt:int = None
        nextCharacter:str = None
        if startIndex < len(s)-1:
            nextCharacter = s[startIndex+1]
            nextRomanInt = romanHash[nextCharacter]

        
        if nextRomanInt is not None and nextRomanInt > currentRomanInt:
            sum += nextRomanInt - currentRomanInt
            startIndex += 2 
            continue

        sum+= currentRomanInt
        startIndex += 1


    return sum


print(romanToInt("MCMXCIV"))