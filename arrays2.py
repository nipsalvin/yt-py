#Getting input for array from user
from array import *

a = array("i",[])

n = int(input("Enter the length of array "))

for i in range(n):
    x = int(input("Enter the next value "))
    a.append(x)

print (a)

#Searching for indexes in array
val = int(input("Enter value to be searched "))

b = 0
for c in a:
    if c == val:
        print(b)
        break

    else:
        print("Not found")
        break

    b += 1

