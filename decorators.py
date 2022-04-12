def divide(x,y):
    if x<y:
        x,y = y,x
    print(x/y)

divide(8,4)

def div (a,b):
    print(a/b)

def smart_div(func): #Create new function that takes 'func' parameter
    def inner(a,b): #Define a function inside a function
        if a<b:
            a,b = b,a
        return func(a,b)
    
    return inner

div = smart_div(div)

div(4,8)