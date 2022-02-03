#Target number
a = 3
x = int (input("How many reps ?"))

i = 1
while i <= x:
    
    #2. Breaks after i becoms greater than a
    if i>a:
        print("Out of stock")
        break
    
    #1.Executes as long as i is less than a
    print ("Strong !!")
    i = i + 1

print("Bye")