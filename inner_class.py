class Student:

    def __init__(self, name, rollno ):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    
    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop: #Creating an inner class
        def __init__(self):
            self.brand = "HP"
            self.cpu = "Core i5"
            self.ram = 6
        
        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student("Alvin", 2) #creating an object of outter class by calling it
s2 = Student("Pinpin", 3)
s2.show()

lap1 = Student.Laptop()#Creating an object (lap1) of inner class(Laptop) by calling it through the outter class (Student)
lap1.show() #Prints data from show method from the inside class
lap2 = s2.lap
lap2.show()
