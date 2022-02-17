from numpy import *

a = array([1,2,3,4])
b = array([2,6,8,10])
#you can use different NumPy functions (e.g max, mean len etc)
print(concatenate([a,b]))

#SHALLOW copying data from another array
#when you copy from another array it is stored in the same register
c = a
print(c)

#copying array to a new register
d = b.view()
print(d)

print(id(a))
print(id(c))
print(id(d))

#DEEP COPYING array
#Copies then remains the same if the first array is changed
e = b.copy()
b[1]=9
print(b)
print(e)
#Stored in different registers
print(id(b))
print(id(e))