
#abbabbabb, bbabbabba, 
def threeLetters(a,b):

    input='aaabbbbbb'

    pass


def helper(input,aConsecutive, bConsecutive, result):
    if len(input) == 0:
        return True

    
    for i in range(len(input)):
        char = input[i]
        if len(result) < 3:
            result.append(char)
        elif result[-1] == result[-2] == char

        helper(input, aConsecutive, bConsecutive, result)



    

