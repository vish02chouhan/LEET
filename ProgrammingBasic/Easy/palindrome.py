

import math

number = 1333
iterationCount = 1
while number > 10:
    number = number //10
    iterationCount +=1

print(10**iterationCount)



#print(math.floor(109))

# 1221

# 1221%10 = 1

# 1221/10 = 122

# 122%10 = 2

# 122/10 = 12

# 12%10 = 2

# 12/10 = 1


1506

# 13231
# --------------------  10000 + 3231
# 13231%10 = 1

# 13231/10 = 1323

# ------------------ 3000 + 231 = 3231

# 1323%10 = 3

# 1323/10 = 132


# ----------------------- 200 + 31
# 132%10 = 2

# 132/10 = 13

# --------------------- 30 + 1

# 13%10 = 3

# 13/10 = 1

class Solution:
    def isPalindrome1(x: int) -> bool:
        if(x<0):
         return False
        xArray = [int(i) for i in str(x)]
        xArrayLen = len(xArray)
        for index in range(0, math.floor(xArrayLen/2)):
            if xArray[index] != xArray[xArrayLen - index - 1]:
                return False

        
        return True

    def isPlaindrome(self,x:int) -> bool:
        remaining = x%10
        divisible = x//10
        nearestMultiple = self.findNearestMultiplier(x)

        reversedNumber

        pass

    def findNearestMultiplier(self,number:int) -> int:
        iterationCount = 1
        while number > 100:
            number = number//10
            iterationCount +=1

        return 10**iterationCount


    #print(isPalindrome(-12121))