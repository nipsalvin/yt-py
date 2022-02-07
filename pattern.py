#method 1
print(" # # # # ")
print(" # # # # ")
print(" # # # # ")
print(" # # # # ")

#method 2

for a in range (4):
    for x in range(4):
        print(" #  ", end="")

    #prints new line
    print()

#pattern 2
for a in range (4):
    for x in range(a + 1):
        print(" #  ", end="")

    #prints new line
    print()

#pattern 2 reverse
for a in range (4):
    for x in range(4 - a):
        print(" #  ", end="")

    #prints new line
    print()
#pattern 4
for a in range (4):
    for x in range(4-a):
        print(1, end="")
    
    print ()

for i in range(1,5):
    for j in range(i,5):
        print( j , end="  ")
    print()

#pattern 5
x = 'ABCD'
y = 'PQR'

for i in range(1, 5):

    print(x[:i] + y[i-1:])