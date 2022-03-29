#method 1
print(" # # # # ")
print(" # # # # ")
print(" # # # # ")
print(" # # # # ")

#method 2
print("Method 2")
for a in range (4):
    for x in range(4):
        print(" #  ", end="")

    #prints new line
    print()

print("Pattern 2")
#pattern 2
for a in range (4):
    for x in range(a + 1):
        print(" #  ", end="")

    #prints new line
    print()

print("Pattern 2 reverse")
#pattern 2 reverse
for a in range (4):
    for x in range(4 - a):
        print(" #  ", end="")

    #prints new line
    print()

print("pattern 4")
#pattern 4
for a in range (4):
    for x in range(4-a):
        print(1, end="")
    
    print ()

print("pattern 5")
#pattern 5
for i in range(1,5):
    for j in range(i,5):
        print( j , end="  ")
    print()

print("pattern 6")
#pattern 6
x = 'ABCD'
y = 'PQR'

for i in range(1, 5):

    print(x[:i] + y[i-1:])

print("My test")
#My Test
for a in range (4):
    for x in range(a + 1):
        print("# ",end="")
    print ()
for a in range (4):
    for x in range(4 - a):
        print("# ",end="")
    print ()