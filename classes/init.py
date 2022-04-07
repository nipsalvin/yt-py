
class Computers:
    
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print("Config is", self.cpu, self.ram)

comp1 = Computers("i5", 16)
comp2 = Computers("Snap Dragon", 8)

comp1.config()
comp2.config()