def stringReversal(str):
    if len(str) <=1:
        return str[0]
    return stringReversal(str[1:])+ str[0] 



print(stringReversal('abcd'))