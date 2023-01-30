

import heapq as hp
def laptopRentals(times):
    times.sort(key = lambda range:range[0])
    mostUsed = 0
    heap = []
    for start, end in times:
        while heap and start >= heap[0]:
            hp.heappop(heap)
        hp.heappush(heap,end)
        mostUsed = max(mostUsed, len(heap))
    return mostUsed

array = [
    [0, 2],
    [1, 4],
    [4, 6],
    [0, 4],
    [7, 8],
    [9, 11],
    [3, 10]
  ]


print(laptopRentals(array))