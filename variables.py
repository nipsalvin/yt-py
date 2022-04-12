class Car:
    
    wheels = 4 #This is a class/static variable

    def __init__(self):
        self.mile = 10 #This is an instance variable
        self.com = "BMW" #This is an instance variable

car1 = Car()
car2 = Car()

car2.com = "Toyota"
car2.mile = 15 
car2.wheels = 5 #Updating value of wheels for car2 only

Car.wheels = 6 #Updating value of wheels globaly

print (car1.com, car1.mile,"Wheels are ",car1.wheels)
print(car2.com, car2.mile,"Wheels are ",car2.wheels)
