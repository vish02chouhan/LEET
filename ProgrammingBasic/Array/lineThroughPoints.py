def lineThroughPoints(points):

    xMin = min([x[0] for x in points])
    xMax = max([x[0] for x in points])


    yMin =  min([x[1] for x in points])
    yMax =  max([x[1] for x in points])

    matrix =  [[0 for x in range(xMin, xMax+1)]for y in range(yMin,yMax+1)]

    for item in points:
        matrix[item[0]][item[1]] = 1

    [[print(item)]for item in matrix]



points= [
  [1, 1],
  [2, 2],
  [3, 3],
  [0, 4],
  [-2, 6],
  [4, 0],
  [2, 1]
]

lineThroughPoints(points)
