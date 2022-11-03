from typing import List

class Solution:
    def pivotIndex1(nums: List[int]) -> int:
        for index in range(1,1):
            print(index)
        return 0

    def pivotIndex2(nums: List[int]) -> int:
        numLength = len(nums)
        sum = 0
        for index,item in enumerate(nums):
            if index == 0:
                sum = 0
            if index > 1:
                sum += nums[index-1]

            innerSum = 0
            for innerItem in range(index+1,numLength):
                innerSum +=nums[innerItem]

            if sum == innerSum:
                return index

        return -1

    def pivotIndex(nums: List[int]) -> int:
        list_sum = sum(nums)
        left_sum = 0
        right_sum = 0

        for i,x in enumerate(nums):
            if i > 0:
                left_sum += nums[i-1]
                
            right_sum = right_sum - x
            
            if right_sum == left_sum:
                return i
             
        return -1



    print(pivotIndex([2,1,-1]))

    