class PyCharm:
    def func(self): #you must have this method for "func" for all objects
        print("Compiling")
        print("Running")

class VsCode:
    def func(self): #you must have this method for "func" for all objects
        print("Spell check")
        print("syntax check") 
        print("Compiling")
        print("Running")
class Laptop:
    def code(self, ide): #you must have this method for "code" for all objects
        ide.func() #you can use the object of the class ide to call the method func of the class ide (ide is the object of the class ide) and it will call the method func of the class ide and it will print the result of the method func of the class ide

ide = PyCharm() #you can choose an IDE here (ide is the object of the class IDE) and it will call the method func of the class IDE and it will print the result of the method func of the class IDE (IDE is the class IDE) 

x = Laptop()
x.code(ide)
