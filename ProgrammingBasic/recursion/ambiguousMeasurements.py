def ambiguousMeasurements(measuringCups, low, high):

    maxMeasurement = high -low
    minMeasurement = low - high
    cache = {}
    result = helper(measuringCups, maxMeasurement, minMeasurement, low, high, cache)
    print(cache)
    return result

def helper(measuringCups,maxMeasurement,minMeasurement, low, high, cache):
    if low < 0 and high < 0:
        return False

    if str(low)+':'+str(high) in cache:
       return cache[str(low)+':'+str(high)]


    for idx in range(len(measuringCups)):
        (currentLow, currentHight) = measuringCups[idx]
        newLow = low - currentLow
        newHigh = high - currentHight
        #print("Low"+":"+str(newLow)+", High:" + str(newHigh))
       # print("maxMeasurement"+":"+str(maxMeasurement)+", minMeasurement:" + str(minMeasurement))
        if minMeasurement <= newLow <= 0  and 0 <= newHigh <=  maxMeasurement:
            return True
        result = helper(measuringCups, maxMeasurement,minMeasurement, newLow, newHigh, cache)
        if result:
            return True

    
    
    cache[str(low)+':'+str(high)] = result
            
    return False
        

        
measurements = [
  [200, 210],
  [450, 465]
]


print(ambiguousMeasurements(measurements, 2100,2300))