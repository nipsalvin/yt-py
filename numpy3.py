#different ways of creating an array
from numpy import *
#Array using array()
#int specifies value type
#using a float type converts all other values to float
a = array([1,2,3,4,5.9],int)

#prints type of values
print(a.dtype)
print("a is ",a)

#Array using linspace()
#0 is the start, 20 is the end 5 is the number of parts(Divisions)
#it uses float type
#if you use without parts it will print 20 parts
b = linspace(0,20,5)
print("b is ",b)
#you can use [n] to specify the value to be printed
print(b[3])

#Array using logspace()
c = logspace(1,40,5)
print("c is ",c)

#Array using zeros() and ones()
#to convert to int we use ,int
d = zeros(5)
e = ones(5,int)

print("d is ",d)
print("e is ",e)