
from math import remainder


def decimalToBinary(number, remainder = ''):
    if number == 1:
        return str(1) + remainder



    remainder +=  str(number%2)
    number = number //2
    remainder = decimalToBinary(number, remainder)
    return remainder


print(decimalToBinary(255))
    