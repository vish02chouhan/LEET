def febonnaci(n):

    if n<= 2:
        return 1

    return febonnaci(n-2) + febonnaci(n-1)


def febonnaciMemozation(n,sumKeys = {}):
    if n in sumKeys:
        return sumKeys[n]

    if n<= 2:
        return 1

    sum =  febonnaciMemozation(n-2,sumKeys) + febonnaciMemozation(n-1,sumKeys)

    if sum not in sumKeys:
        sumKeys[n] = sum

    return sum

def febonnaciLoop(n):

    first = 0
    second = 1
    nth = first + second

    for i in range(2, n):
        nth = first + second
        first = second
        second = nth

    return nth






# if n == 1

# n= 1 ,febonnaci(1) = 1

# n= 2 ,febonnaci(2) = 2

# n=3, febonnaci(2) + febonnachi(1) 1 = 1

# n=3 febonnaci(1) + febonnachi(2) 1 = 1

#print(febonnaci(35))

#print(febonnaciLoop(51))

print(febonnaciMemozation(50))










#6-

#0 1 1 2 3 5