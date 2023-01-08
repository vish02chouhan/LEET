
def ambiguousMeasurements(measuringCups, low, high):
    # Write your code here.
    return False


measuringCups = [
    [200, 210],
    [450, 465],
    [800, 850]
  ]
low = 2100,
high = 2300

#200 * 10 , 210 * 10 (2000, 2100)
    #200 * 10 + 200 * 1 , 210 * 10 + 210 * 1 (2200, 2310)
    #200 * 10 + 450 * 1 , 210 * 11 + 465 * 1 (its not in range) 
    #200 * 10 + 800 * 1 , 210 * 11 + 850 * 1 (its not in range) 

     #200 * 9 + 450 * 1 , 210 * 10 + 465 * 1 (2200, 2310)

     #200 * 8  , 210 * 8  (1600, 2310)

    #200 * 1 + 450*3, 210 * 1 + 465 * 3

ambiguousMeasurements(measuringCups, low, high)