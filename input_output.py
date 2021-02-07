# List of codes for taking standard inputs and returning standard outputs
# Reference: https://qiita.com/jamjamjam/items/e066b8c7bc85487c0785

# Take an input as a string
s = input()
# Take an input as an integer
i = int(input())
# Take an input as a float
f = float(input())

# If standard input has 2 or more strings
# Take input as a list
ss = input().split()

'''
# If input is [Alice Bob Charlie]
then,
>>>print(ss)
['Alice', 'Bob', 'Charlie']
>>>print(ss[0])
Alice
>>>print(ss[0][0])
A
'''

# Take input as separated strings
A, B, C = input().split()

'''
# outputs looks like
>>>print(A)
Alice
>>>print(A,B,C)
Alice Bob Charlie
'''

# If standard input has 2 or more integers
# Take input as separated integers
A, B = map(int, input().split())

'''
# outputs looks like
>>>print(A)
1
>>>print(A,B)
1 3
'''

'''
How to use map()

The map function is a higher-order function that applys the operations of
an arbitrary function to all the components of a sequence.

map(callable object, iterable object)

callable object: class, function
iterable object: list, tuple, etc.

'''

# Take the input as a List
l = list(map(int, input().split()))

'''
# outputs looks like
>>>print(l)
[1, 3, 4, 5, 6]
'''

# If inputs contains both numbers and strings
N, S = map(str, input().split())

N, M = map(int, input().split())
#リスト内包表記
A = [int(input()) for _ in range(M)]

# If inputs have two lists and want to combine them.
# for example
'''
N
x1 y1
x2 y2
. .
. .
. .
xn yn
'''
# using numpy
import numpy as np
N = int(input())
xy = []
for _ in range(N):
    xy.append(np.array([int(i) for i in input().split()]))

# without numpy
N = int(input())
xy = []
for i in range(N):
  x, y = map(int, input().split(' '))
  xy.append([x, y])
