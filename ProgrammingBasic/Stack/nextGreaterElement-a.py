def nextGreaterElement(array):    
    result = [-1] * len(array)    
    stack = []    
    for idx in range(2 * len(array)):        
        circularIdx = idx % len(array)        
        while len(stack) > 0 and array[stack[-1]] < array[circularIdx]:            
            top = stack.pop()            
            result[top] = array[circularIdx]        
        
        stack.append(circularIdx)    
        
    return result


print(nextGreaterElement([2, 5, -3, -4, 6, 7, 2]))