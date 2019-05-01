import math


def calcDifference(arr, avgarr, factornumber):
    distance = 0
    for i in range(0, len(arr)):
        distance += math.pow(arr[i]-avgarr[i]+factornumber, 2)
    return int(math.sqrt(distance))

def find_nearest(matrix, Tiles ):
    newarr = []

    for i in range(0, len(Tiles)):
        smallestDifference = calcDifference(matrix, Tiles[0], 0)
        minIndex = 0
        for j in range(1, len(Tiles)):
            tempDifference = calcDifference(matrix, Tiles[j], 0)
            if tempDifference < smallestDifference:
               minIndex = j
               smallestDifference = tempDifference
        newarr.append(minIndex)