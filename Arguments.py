def person(name, age): #Formal Argument
#def person(name, age=18) #3. Actual argument using Default values
    print(name)
    print(age-5)

#Actual arguments
#Types
person("Alvin", 27) #1. Using Position
person(age=27, name="Alvin") #2. Using Keywords

#4. Actual arguments using variable length
def var(a, *b):
    c = a
    for i in b:
        c = c + i
    print(c)
var(2,4,50)

#4.2. Actual arguments using variable length method 2
def var2(*d):
    e = 0
    for j in d:
        e = e + j
    print (e)
var2(1,2,3,4,5)