a = 10


def local():
    #This is declaring that a is the global variable
    #global a
    a = 15
    print("Local", a)
    print(id(a))
    x = globals()['a']
    print("Global 'a' in Local 'x'", x)
    print(id(x))

local()
print("Global", a)
print(id(a))
