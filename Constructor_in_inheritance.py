class A:
    def __init__(self):
        print("class A init")
    def feature1(self):
        print("Feature 1-A working")
    
#super inherits from super clas
class B(A): #B inherits from A
    def __init__(self):
        super().__init__()#B inherits init from A
    def feature1(self):
        print("Feature 1 working")

class C(A):#C inherits from A
    def __init__(self):
        super().__init__()#Inherits  init from A
        print("class C init")#executes its own init

class D():
    def __init__(self): #defined init method inside class
        print("class D init")
    def feature1(self):
        print("Feature 1-D working")
    def feature4(self):
        print("Feature 4 working")

class E(A,D): #inherits from both A and D
    def __init__(self):
        super().__init__() #Calls init from A (MRO)
    def feature5(self):
        super().feature1

x = E()
x.feature1() #calls from super class A
x.feature4() #calls from super class D