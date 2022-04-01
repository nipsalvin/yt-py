from array import *

vals = array("i",[8,3,-7,2,9,3,-6,5])
vals2 = array("f",[3.3, 4.5,3.54])

print (vals.buffer_info())
print (vals2.typecode)
print(vals.typecode)

#printing value at position
print (vals2[0])
print("End of printing value at position 0")

#using a loop with the array
for i in range(5):
    print(vals[i])
print("End of array with for loop to position 5")
#printing all values in the array one at a time
for a in range(len(vals)):
    print (vals[a])
print("End of range. prints 8 values (length of vals) 1 at a time")

#printing all values in the array one at a time(method 2)
for b in vals:
    print (b)
print("End of prints values in vals one at a time")

#creating new array with same values
newArray = array(vals.typecode,(c for c in vals))

for d in newArray:
    print(d)
print("Printing d that picks values from newArray which gets values from vals")

#creating new array with same values but new function
newArray2 = array(vals.typecode,(e*e for e in vals))

for f in newArray2:
    print(f)
print("Printing f that picks values from newArrays which gets values from vals but with function")

#printing values of an array using while loop
g = 0
while g<len(newArray):
    print(newArray[g])
    g += 1
print("Prints g using a while loop that picks values from newArray")