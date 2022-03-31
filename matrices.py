#performing functions with array
from numpy import *

#creating a 2D array with array
a = array([
    [1,2,3],
    [3,4,5]
        ])

print("Default array a",a)
#Prints the size of the array
print("A-size is ",a.size)
#Prints the number of rows/columns
print("A-Shape is ", a.shape)

#Converts a 2D array into a 1D array
b = a.flatten()
print("b is a-flattened which is ",b)

#Creating a multi dimensional array using matrix
c = matrix([
    [1,2,3,4],
    [2,3,4,5],
    [3,4,5,6]
])

print ("c matrix is: ", c)

d = matrix('1 2 3; 3 4 5; 6 7 8')
e = matrix('2 3 4; 4 5 6; 7 8 9')
#multiplying matrices
x = d * e

print("d matrix is: ",d)
print("e matrix is: ",e)
print("x (d*e) is equal to \n" ,x)
