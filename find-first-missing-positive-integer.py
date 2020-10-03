""" 
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place. 
"""
from bisect import bisect_right
originalIntegerList = [-98, 37, -4, 1, 2, 2, 4, 6, 7]

def find_first_missing_positive_integer():
    originalIntegerList.sort()
    i = bisect_right(originalIntegerList,0,0,len(originalIntegerList))
    if originalIntegerList[i] != 1:
        return 1
    else:
        lastNumber = 1
        while i < len(originalIntegerList):
            if ((originalIntegerList[i]-lastNumber == 0) or (originalIntegerList[i]-lastNumber == 1)):
                lastNumber=originalIntegerList[i]
                i+=1
            else:
                return lastNumber + 1

print("First missing positive integer is " + str(find_first_missing_positive_integer()))