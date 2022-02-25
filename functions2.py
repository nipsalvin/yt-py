#First example
def func(x):
    x = 8
    print("x is ", x)


a = 15
func(a)
print("a is ", a)

#example 2
def func2(b):
    print(b)

    b[1] = 20
    print(id(b))

b = [1, 2, 3, 4, 5]
print(id(b))
func2(b)
print("b is", b)