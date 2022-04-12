class People:
    
    def __init__(self):
        self.age = 20
        self.name = "Alvin"

    def new(self):
        self.age = 25
        self.name = "Nips"

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

x = People()
y = People()

y.name = "PinPin"
x.age = 30

print(x.name, x.age)
print(y.name, y.age)

x.new()
print(x.name, x.age)

x1 = People()
y1 = People()
if x.compare(y):
    print("They are same")
else:
    print("They are not the same")