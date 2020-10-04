""" 
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr 

"""
#Given Implementation To Construct Pair
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

#Return first value in closure returned from given cons implementation
def car(pair):
    return pair.__closure__[0].cell_contents

#Return last value in closure returned from given cons implementation
def cdr(pair):
    return pair.__closure__[1].cell_contents

assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4
print("Process completed successfully")