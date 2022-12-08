
from typing import List

#nums = [2,7,11,15], target = 9

#solution 1 -> 
# loop through array , loop inside loop and sum all elements except where 
# inner loop index not equal to outer loop index and check with sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i]+ nums[j] == target:
                    return [i,j]

        return [-1,-1]
    # will create a dictionary and store elemnt of array in it , 
    #if it doent exist in dictionary
    #every elemt we subract from target and try to find remaning in dictionary
    #if remaining is another elemnt in dictionary than its value
    # which is index will be the answer
    def twoSumDict(self, nums: List[int], target: int) -> List[int]:

        numsDictionary = {}
        for idx, item in enumerate(nums):
            remaining = target - item
            if remaining in numsDictionary:
                return [numsDictionary[remaining], idx]
            else:
                numsDictionary[item]= idx

        return [-1,-1]
            

sol = Solution()

print(sol.twoSumDict([3,2,4], 6))

        
