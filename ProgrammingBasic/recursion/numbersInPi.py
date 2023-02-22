def numbersInPi(pi, numbers):
    numbers = set(numbers)
    return helper(pi, numbers, -1, 0)


def helper(pi, numbers, count, index):
    if index == len(pi):
        return count
    
    minCount = float('inf')
    for i in range(index, len(pi)):
        word = pi[index:i+1]
        print(word)
        if word in numbers:
            result = helper(pi, numbers, count+1, i+1)
            print(f"result:{result}")
            minCount = min(result, minCount)
 

    return minCount
            
        
        
        
pi = "3141592653589793238462643383279"
numbers = ["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]

numbersInPi(pi,numbers)