from math import fabs


class Solution:
    def isValid(s: str) -> bool:
        openItems = ['(','{','[']
        closeItems = [')','}',']']
        openCloseItems = {')':'(','}':'{',']':'['}
        itemArray = []

        
        if(len(s) <= 1):
            return False

        for item in s:
            if len(itemArray) == 0 and item in closeItems:
                return False

            if item in openItems:
                itemArray.append(item)
            #item is in close
            else:
                popedItem = itemArray.pop()
                print(popedItem)
                print(openCloseItems[item])
                if popedItem != openCloseItems[item]:
                    return False
        if(len(itemArray) > 0):
            return False
        return True

    isValid('()')
                            