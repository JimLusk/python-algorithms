""" 
Algorithm Objective
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division? 
"""


originalNumberList = [1, 2, 3, 4, 5]
resultNumberList = []

def construct_array_product_sans_current():
    #calculate product of all numbers in given set
    for i in range(len(originalNumberList)) :
        if i==0:
            result = originalNumberList[i]
        else:
            result=result * originalNumberList[i]
    for j in range(len(originalNumberList)) :
        resultNumberList.insert(j, result/originalNumberList[j])
    return resultNumberList
    
print("Original Number List: " + str(originalNumberList))
print("Result Number List: " + str(construct_array_product_sans_current()))


        
        
