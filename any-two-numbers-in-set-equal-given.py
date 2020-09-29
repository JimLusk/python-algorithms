""" 
Algorithm Objective
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass? 
"""

# 1. Create a variable to hold set of numbers to traverse and iterator count variables to use for nested count variables.
# 2. Iterate over set adding 1s number in set to all that follow in set, if it equals given return true.
def check_set_for_desired_sum (sumTargetAnyTwo):
    #initialize variable to hold list of numbers to traverse
    numberList = [10, 15, 3, 7]
    print ("Number List: " + str(numberList))
    print ("Sum Of Any Two Numbers Target: " + str(sumTargetAnyTwo))
    #initialize iterator variables to assist with the check
    length= len(numberList)
    iter1 = 0
    iter2 = 0
    #outer iterator is going to go through every number in the list
    for number in numberList:
        #nested iterator is going to go through every number in list *after* current set
        iter2 = iter1 + 1
        while iter2 < length:
            targetValue = number + numberList[iter2]
            if targetValue == sumTargetAnyTwo:
                return True
            iter2 = iter2 + 1
        iter1 = iter1 + 1
    return False

print ("Does sum of any two numbers equal target? => " + str(check_set_for_desired_sum(17)))
