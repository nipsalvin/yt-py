from traceback import print_tb


fname = input ("Enter First Name ")
lname = input ("Enter Last Name ")

name = fname + ' ' + lname
print(name)
#prints first character
print(name[0])

x = input("First Number ? ")
int (x)
y = input("Second Number ? ")
int (y)
z = y + x
print (z)

#prints evaluation
result = eval(input("Enter marks? "))
if result > 50:
    print("pass")
elif result == 50:
    print("median")
else:
    print("Fail")
#print(result)