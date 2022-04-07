class Computer:

    def stats(self):
        print("Computer is i5, 16gb RAM, 1tb Storage")
    
    def stats2(self):
        print("Computer is i7, 16gb RAM, 500gb Storage")

comp1 = Computer() #Defines comp1 variable as an object of Computer class.
comp2 = Computer() #Defines comp1 variable as an object of Computer class.

#These 2 can run without defining object as variable of class
Computer.stats(comp1) #Call computer class then stats method then defines comp1 as the argument
Computer.stats2(comp2) # In layman's: Hello "Computer" I want your "Stats" for "comp2"

#In these 2 the object has to be defined as a variable of class
comp1.stats2() #Using the object to call the method
comp2.stats() 