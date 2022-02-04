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