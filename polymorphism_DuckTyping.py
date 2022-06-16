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
    def code(self, ide):
        ide.func()

ide = PyCharm() #you can choose an IDE here

x = Laptop()
x.code(ide)
