#BBC
def runLengthEncoding(string):
    output = []
    current = 0
    sum = 1
    character = None
    while current + 1 < len(string):
        character = string[current]

        # if current + 1 == len(string):
        #    if string[current] != string[current-1]:
        #         output.append(character)
        #     else:
        #    break
          
            
        if string[current] == string[current+1]:
            sum += 1
        else:
            itemMultiples = sum//9
            remainder = sum % 9 

            for count in range(itemMultiples):
                output.append('9'+ character)
            
            if remainder > 0:
                output.append(str(remainder)+character)

            sum = 1
            character = None
        current += 1

    if character:
            itemMultiples = sum//9
            remainder = sum % 9 

            for count in range(itemMultiples):
                output.append('9'+ character)
            
            if remainder > 0:
                output.append(str(remainder)+character)

    return ''.join(output)

print(runLengthEncoding('AAAAAAAAAAAAABBCCCCDD'))