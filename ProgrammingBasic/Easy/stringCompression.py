from typing import List


class Solution:
   def compress(self, chars: List[str]) -> int:

    count = None
    char = None
    output = []

    for item in chars:
        if count is None:
            count = 1
            char = item
        else:
            if char != item:
                output.append(char)
                if count > 1:
                    output.append(str(count))
                count = 1 
                char = item
                
            else:
                count += 1


    if count is not None:
        output.append(char)
        if count > 1:
            output.append(count)

    return output

sol = Solution()
print(sol.compress(["a","a","b","b","c","c","c"]))