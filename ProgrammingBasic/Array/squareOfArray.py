import this


def sortedSquaredArray(array):
    newArray = [item*item for item in array]
    newArray.sort()
    return newArray



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 10
print(thisdict)

