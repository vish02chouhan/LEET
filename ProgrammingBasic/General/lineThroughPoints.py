from fractions import Fraction

def lineThroughPoints(points):
    maxLinesThroughPoints = 1
    
    # Begin iteration
    for i in range(len(points)-1):
        x1, y1 = points[i]
        slopesDictionary = {}
        for j in range(i+1, len(points)):
            x2, y2 = points[j]
            # Find slope of pair of lines
            slope = Fraction(y2-y1, x2-x1) if x1 != x2 else float("inf")
            numerator, denominator = (1, 0) if slope == float("inf") else (slope.numerator, slope.denominator)
            if (numerator, denominator) not in slopesDictionary:
                slopesDictionary[(numerator, denominator)] = 1
            slopesDictionary[(numerator, denominator)] += 1
        # Update maximum number of lines found through pivot point
        maxLinesThroughCurrentPivot = max(slopesDictionary.values())
        maxLinesThroughPoints = max(maxLinesThroughPoints, maxLinesThroughCurrentPivot)
    return maxLinesThroughPoints


points =  [
    [1, 1],
    [2, 2],
    [3, 3],
    [0, 4],
    [-2, 6],
    [4, 0],
    [2, 1]
  ]

lineThroughPoints(points)



