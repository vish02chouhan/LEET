from typing import List

       
class Solution:
    def longestCommonPrefix(strs: List[str]) -> str:
        prefix = ""
        for index,item in enumerate(strs[0]):
            prefix += item

            for innerIndex in range(1, len(strs)):
                print(str(innerIndex))
                print(strs[innerIndex][0:index+1])
                if prefix != strs[innerIndex][0, index]:
                    return ""

        return prefix

    
    longestCommonPrefix(["flower","flow","flight"])




