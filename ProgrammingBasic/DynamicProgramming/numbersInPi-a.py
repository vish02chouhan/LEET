def numbersInPi(pi, numbers):
    count, minCount = piCountHelper(pi, numbers, 0,float('inf'))
    print(minCount)


def piCountHelper(pi, numbers, count, minCount):
    if len(pi) == 0:
        return count, minCount

    count = 0
    newPi = ""
    for i in range(len(numbers)):
        if i == 1:
            st = 0
        if pi.startswith(numbers[i]):
            newPi = pi[len(numbers[i]):]
            newArray = numbers[:i] + numbers[i+1:]
            count += 1
            count, minCount = piCountHelper(newPi, newArray, count, minCount)
            if len(newPi) == 0:
                minCount = min(minCount, count)

    
    return count, minCount


pi = "3141592653589793238462643383279"
numbers = ["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]
#output 2 - // "314159265 | 35897932384626433832 | 79"
numbersInPi(pi, numbers)
# if pi.startswith('314159265358979323846'):
#     pi = pi[len('314159265358979323846'):]
#     print(pi)


# 314159265358979323846
# 26433
# 8
# 3279