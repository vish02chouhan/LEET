from typing import List

for i in range(10 - 3, -1, -1):
    print(i)


class Solution:
     

    def largestPerimeter(self, nums: List[int]) -> int:
        sum = 0
        for idx,x in enumerate(nums):
            if x+2 >= len(nums):
                break
            currentSum = self.largestPerimeterHelper([nums[x],nums[x+1], nums[x+2]])
            if currentSum > sum:
                sum = currentSum
        return sum

    def largestPerimeterHelper(self, nums: List[int]) -> int:
        if nums[0] + nums[1] <= nums[2]:
            return 0
        
        if nums[1] + nums[2] <= nums[0]:
            return 0
        
        if nums[0] + nums[2] <= nums[1]:
            return 0

        return nums[0] + nums[1] + nums[2]

    
    