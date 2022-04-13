#Company is Toyota (Class)
#car 1 & 2 are models (Objects)

class Toyota:
    
    wheels = 4 #This is a class/static variable

    def __init__(self):
        self.mile = 10 #This is an instance variable
        self.make = "Prado" #This is an instance variable

car1 = Toyota()
car2 = Toyota()

car2.make = "Premio"
car2.mile = 15 
car2.wheels = 5 #Updating value of wheels for car2 only

Toyota.wheels = 6 #Updating value of wheels globaly 

print (car1.make, car1.mile,"Wheels are ",car1.wheels)
print(car2.make, car2.mile,"Wheels are ",car2.wheels)
