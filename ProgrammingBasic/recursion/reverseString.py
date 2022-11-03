def reverseString(input):
    if input == "":
        return ""

    
    newString = reverseString(input[1:])

    mergedString = newString + input[0]

    return mergedString


print(reverseString('hello'))