class A: #This is the parent class
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B(A): #This inherits from class A (Single level inheritance)
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")

class C(B):# This inherits from class B which has inherited from A (Multilevel inheritance)
    def feature5(self):
        print("Feature 5 working")
    def feature5(self):
        print("Feature 6 working")
    
class D:
    def feature7(self):
        print("Feature 7 working")
    def feature8(self):
        print("Feature 8 working")

class E(A,D): #This inherits from class A and class D (Multiple Inheritance)
    def feature9(self):
        print("Feature 9 working")
    def feature10(self):
        print("Feature 10 working")
        
v = A()
w = B()
x = C()
y = D()
z = E()


v.feature2()
w.feature2()
x.feature2()
y.feature7()
z.feature10()