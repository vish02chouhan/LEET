
from typing import List

dict ={ "a":1 , "b":2 , "c":3}

dict["a"] = 5

print(dict["a"])

class Solution:
    def runningSum1(nums):
        numLength = len(nums)
        for index in range( 3,4):
            print("Index: " + str(index) + "item " + str(nums[index]))

    def runningSumWithoutDict(nums, target):
        numLength = len(nums)
        for index,item in enumerate(nums):
            
            for innerIndex in range (index+1, numLength):
                if target == item + nums[innerIndex]:
                    return[index,innerIndex]

        return [-1,-1]

    def runningSum(nums, target):
        numLength = len(nums)
        dict={}

        for index,item in enumerate(nums):

            if target - item in dict:
                return dict[target-item]                   
            dict[item] = index

        return [-1,-1]
    
    print(runningSum([1,3,7,4],8))


    

