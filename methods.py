class Student:

    school = "School of Nips"  #Static/Class variable. It is used in the whole class

    def __init__(self, m1, m2, m3, m4): #parsing 3 objects
        self.m1 = m1 # m1, m2, m3 are instance variables
        self.m2 = m2 # They are used only when this method is called
        self.m3 = m3
        self.m4 = m4
    
    def avg(self): #creating a STATIC method to find average
        return(self.m1 + self.m2 + self.m3 + self.m4)/4

    def get_m1(self): #ACCESSOR Methods. Fetches values in variables
        return self.m1

    def get_m2(self):
        return self.m2

    def get_m3(self):
        return self.m3
    
    def set_m2(self,value): #MUTATOR method. Changes values in variables
        self.m2 = value
        return self.m2

    @classmethod #Decorator
    def getSchool(cls): #This is a class method.
        return cls.school

    @staticmethod
    def info(): #This is a static method
        print("This is an example of a static method")

a1 = Student(70,80,75,85)
a2 = Student(50,60,55,65)


print(a1.get_m1())
print(a1.avg())
print(a1.set_m2(45))
print(a1.avg())
print(Student.getSchool())
Student.info()


