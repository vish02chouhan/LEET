import functools

def minDifficulty(A, d):
    n = len(A)
    if n < d: return -1

    #@functools.lru_cache(None)
    def dfs(i, d):
        #print(f"i:{i},A[i]:{A[i]} d:{d}")
        if d == 1:
            return max(A[i:])
        res, maxd = float('inf'), 0
        for j in range(i, n - d + 1):
            maxd = max(maxd, A[j])
            print(f"sMaxd:{maxd}")
            dres = dfs(j + 1, d - 1)
            print(f"i:{j},maxd:{maxd}, dres:{dres}, res:{res}")
            res = min(res, maxd + dres)
            print(f"res:{res}")
        return res
    return dfs(0, d)

array =[2,4,8,1,3,9,2,6,9]
days = 4

print(minDifficulty(array, days))



