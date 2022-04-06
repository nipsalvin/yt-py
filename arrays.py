from array import *

vals = array("i",[8,3,-7,2,9,3,-6,5])
vals2 = array("f",[3.3, 4.5,3.54])

print (vals.buffer_info())
print (vals2.typecode)

#printing values 1 at a time
print (vals2[0])

#using a loop with the array
for i in range(5):
    print(vals[i])

#printing all values in the array one at a time
for a in range(len(vals)):
    print (vals[a])

#printing all values in the array one at a time(method 2)
for b in vals:
    print (b)

#creating new array with same values
newArray = array(vals.typecode,(c for c in vals))

for d in newArray:
    print(d)

#creating new array with same values but new function (Square root)
newArray2 = array(vals.typecode,(e*e for e in vals))

for f in newArray2:
    print(f)

#printing values of an array using while loop
g = 0
while g<len(newArray):
    print(newArray[g])
    g += 1