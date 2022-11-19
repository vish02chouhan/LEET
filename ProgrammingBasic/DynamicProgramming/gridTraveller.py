def gridTraveller(height, width ):

    if height == 0 or width == 0:
        return 0
    
    if height == width == 1:
        return 1

    return gridTraveller(height - 1, width) + gridTraveller(height, width - 1)



print(gridTraveller(18,18))