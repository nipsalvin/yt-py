class Student:

    school = "School of Pipsology"

    def __init__(self, m1, m2, m3, m4):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
    
    def avg(self): #Instance method that works with instance variable
        return(self.m1 + self.m2 + self.m3 + self.m4)/4

    @classmethod #Decorator for class method
    def getSchool(cls): #Works with class variable
        return cls.school

    @staticmethod #Decorator for static method
    def info(): #Work with 
        print("This is student class in static method")
    
s1 = Student(10,20,30,40)
s2 = Student(15,25,35,45)

print (s1.avg())
print (s2.school)

print(Student.getSchool())

Student.info()