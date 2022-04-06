def fib(n): #Define Function
    a = 0   #Define variables
    b = 1   #Define variables

    if n < 1:
        print ("Too low") 
    else:
        print(a)
        print(b)

        for i in range(2,n): #For values in 2nd position to Nth position

            c = a + b
            a = b
            b = c
            if c >= 100: 
                break #Breaks loop if value of the fibonacci goes over 100
            print(c)

fib(int(input("Enter length of fibonacci sequence ")))