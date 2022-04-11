class Cars:     #Define class
    def __init__(self, name, model, color): #initialize method with name, model and color variables
        self.name = name #Assign values to variables
        self.model = model
        self.color = color
    
a = input("Enter car name: ")
b = input("Enter car model: ")
c = input("Enter color: ")

print(c, a, b)

d = Cars(a, b, c)
print(f"You want a {d.name} model {d.model} of color {d.color}") #Calls variables from __init__ function in Class

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def func(self):
        print(f"The missing person is {self.name} of age {self.age}")

a = input("Enter name of person: ")
b = input("Enter age: ")

x = People(a, b)
x.func()
