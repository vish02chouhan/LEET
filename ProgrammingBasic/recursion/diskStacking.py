def diskStacking(disks):
    output = [[]]
    helper(disks,output)
    print(output)

def helper(disks,output):
    if len(disks) == 0:
        return [[]]

    
    for i in range(len(disks)):
        
        currentDisk = disks[i]
        currentOutput = [currentDisk]
        remainingDisks = disks[:i] + disks[i+1:]
        diskWithGreaterDimension = filterDisksWithGreaterWDH(currentDisk, remainingDisks)
        results = helper(diskWithGreaterDimension, output)
        
        for item in currentOutput:
            for result in results:
                item = item + result

        output.append(currentOutput)

    return output
    
def filterDisksWithGreaterWDH(currentDisk, remainingDisks):
    filteredDisks = []
    for disk in remainingDisks:
        if disk[0] > currentDisk[0] and disk[1] > currentDisk[1] and disk[2] > currentDisk[2]:
            filteredDisks.append(disk)

    return filteredDisks


disks = [
  [2, 1, 2],
  [3, 2, 3],
  [2, 2, 8],
  [3, 3, 4],
  [1, 3, 1],
  [4, 4, 5]
]


diskStacking(disks)