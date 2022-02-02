x = 33.9
r = x % 2
if r == 0:
    print("Even")
    if x > 30:
        print("Greater")
    else:
        print("Less")

else:
    print("Odd")
    if x > 3:
        print("Greater")
    else:
        print("Less")

#Nested if
if r == 1:
    print("One")
elif (r == 0):
    print("Zero")
else :
    print("Error")
