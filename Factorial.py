def fact(n):

    f = 1
    for i in range(1,n+1): #n+1 to end the loop at the value given by user
        f=f*i
    return f  

x = int(input("Enter length of factorial "))
result= fact(x)
print(result)

