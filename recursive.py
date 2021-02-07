#! usr/bin/env python3

# Recursive function

'''
def myfunc(x):
    if termintation condition:
        return x
    // perform calculation
    myfunc(x)

'''

# this is one of the built-in funtion all()
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

'''
You can use all() function in while loop.

count
while all(condition for i in n):
    do calculation
    count += 1


this code can iterate "calculation", while i satisfies the "condition".
Also, we can count how many times we did iteration.

'''
