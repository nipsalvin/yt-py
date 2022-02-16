from numpy import *
#Array using array()
#int specifies value type
a = array([1,2,3,4,5.9],int)

#prints type of values
print(a.dtype)
print(a)

#Array using linspace()
#0 is the start, 20 is the end 5 is the number of parts(Divisions)
#it uses float type
#if you use without parts it will print 20 parts
b = linspace(0,20,5)
print(b)

