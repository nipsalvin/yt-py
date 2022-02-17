#performing functions with array
from numpy import *

#creating a 2D array with array
a = array([
    [1,2,3],
    [3,4,5]
])

print(a)
#Prints the size of the array
print(a.size)
#Prints the number of rows/columns
print(a.shape)

#Converts a 2D array into a 1D array
b = a.flatten()
print(b)

#Creating a multi dimensional array using matrix
c = matrix([
    [1,2,3,4],
    [2,3,4,5],
    [3,4,5,6]
])

print (c)

d = matrix('1 2 3; 3 4 5; 6 7 8')
e = matrix('1 2 3; 3 4 5; 6 7 8')
#multiplying matrices
x = d * e

print(d)
print("x is equal to \n" ,x)
