from numpy import *

a = array([1,2,3,4])

b = a.view()
c = a.copy()

a[2] = 7
print(a)
print(b)
print(c)