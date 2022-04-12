
class People:
    
    def __init__(self):
        self.age = 20 #First definition of age
        self.name = "Alvin" #First definition of name

    def new(self):
        self.age = 25 #New definition of age
        self.name = "Nips" #New definition of name

    def compare(self, other): #Function for comparison
        if self.age == other.age: #Comparing if 2 'ages' are alike
            return True
        else:
            return False

x = People() #Creating object from class People
y = People() #Creating object from class People

y.name = "PinPin" #New definition of name (y.name)
x.age = 30 #New definition of age (x.age)

print(x.name, x.age)
print(y.name, y.age)

x.new() #New definition of x using function "new"
print(x.name, x.age)

x1 = People()
y1 = People()
if x1.compare(y1): #Comparing 2 objects
    print("They are same")
else:
    print("They are not the same")