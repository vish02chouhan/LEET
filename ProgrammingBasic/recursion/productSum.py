def productSum(array,total = 0):
    return calculate(array)


def calculate(array, index = 2):
    total = 0
    for item in array:
        if type(item) == type([]):
           total = total + (index * calculate(item, index+1))
        else:
            total += item

    return total


print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))