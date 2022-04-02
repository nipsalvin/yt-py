name_list = [] #Create an empty list
def solution(): #Create function
    n = int(input("Enter number here ")) #Create empty variable 'n' to get input(int) from user
    for a in range(1,1+n): #Iterate through the loop until values in 'a' are the same number as '1+n' starting from 1st value
        a = input("Enter name here ") #asks for input from user
        name_list.append(a) #appends the empty list (name_list) with input from the user
    more = [] #create empty list 'more'
    less = [] #create empty list 'less'

    for x in name_list: #iterates through the 'name_list' picking one value at a time
        if len(x) >= 5: #checks if length of 'x' is greater or equal to 5
            more.append(x) #if 'x' is greater than 5 then 'more' list is appended
            print(x)
        else:
            less.append(x) #if 'x' is less than 5 then 'less' list is appended
            print(x)
    print("n is",n,". a is",a,". More is",more,". Less is",less, "x is",x)
    print(name_list)
solution()
