def numberOfWaysToTraverseGraph(height, width):
    matrix = [[1 if y ==0 or x ==0 else 0 for y in range(width)] for x in range(height)]
    print(matrix)

    for h in range(1,height):
        for y in range(1,width):
            matrix[h][y] = matrix[h-1][y] + matrix[h][y-1]

    
    return matrix[-1][-1]


print(numberOfWaysToTraverseGraph(4,3))