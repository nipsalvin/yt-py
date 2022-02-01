#Seapping variables

#Assigning Variables
a = 5
b = 6

#Method 1
temp = a
a = b
b = temp

#Method 2
a = a + b
b = a - b
a = a - b

#method 3. This does not waste any bit
a = a ^ b
b = a ^ b
a = a ^ b

#method 4
a,b = b,a

print (a)
print (b)