#Defining the function
from unittest import result


def func():
    print("Yess")

#Defining function with multiple arguments
def func2(x,y):
    c = x+y
    print(c)

#Defining a value that you expect a response
def func3_func4(u,v):
    d = u+v
    e = u-v
    return e,d

#calling your function
func()
func2(4,5)

result = (func2(4,5))
print (result)

#When returning 2 values you have to accept result 2
result1, result2 = func3_func4(10, 5)
print(result1)
print(result2)
print(result1,result2)