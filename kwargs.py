def person(name, **details):#1. * is to accept multiple arguments. **parsing multiple arguments with the help of key words
    print (name)
    print(details)
    #To print individual items
    for i,j in details.items():
        print(i,j)

person(name = "Nips", age = 27, Location = "Nairobi", Number = 123456789)
