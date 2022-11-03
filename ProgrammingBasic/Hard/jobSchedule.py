from functools import lru_cache
from math import inf
from typing import List

# [3, 5, -4, 8, 11, -1, 1, 6]
# targetSum 10
def twoNumberSum(array, targetSum):

    elementAndIndex = {}
    for index,item in enumerate(array):
        if targetSum - item in elementAndIndex:
            return [elementAndIndex[item], index]

        elementAndIndex[item]=index

    return [-1,-1]


#[11,111,22,222,33,333,44,444]
class Solution:
    def minDifficulty(jobDifficulty: List[int], d: int) -> int:
        
       # @lru_cache(None)
        def dp(idx,d,curr):
            #print("idx:" + str(idx) +", d:"+ str(d) + ", curr:"+ str(curr))
            if idx == len(jobDifficulty) and d == 0: return curr
            if idx >= len(jobDifficulty) or  d <= 0: return inf
            
            firstStep = dp(idx+1,d,max(curr,jobDifficulty[idx]))
            #print("first step:" + str(firstStep))
            lastStep = min(
                       firstStep,
                       max(curr,jobDifficulty[idx]) + dp(idx+1,d-1,0)
                       )
            if lastStep != inf:
                print("last step:" + str(lastStep))
            return lastStep
       
        ans = dp(0,d,0)

        return ans if ans != inf else -1
    
    print(minDifficulty([11,111,22,222,33,333,44,444],6))