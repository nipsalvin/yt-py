a = 6
b = 4

print(int.__add__(a, b)) #Int is a class. __add__ is a method in class Int

x = "Hello"
y = " World"

print(str.__add__(x, y)) #This is what gets called when you use the + operator

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3
    
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False
    
s1 = Student(56, 89)
s2 = Student(90, 78)
s3 = s1 + s2 #This doesn't work until __add__ is defined in the class

print(s3.m1) #adds both m1s of s1 and s2

x = 9
print (x.__add__(10)) #adds 10 to x

if s1 > s2: #This doesn't work until __gt__ is defined in the class
    print("s1 is greater") 
else:
    print("s2 is greater")
