#For IDLE
keys = [1, 2, 3, 4]
values = ["Name", "Age", "Height", "Weight",]

#Dict assigns values to keys
assignment = dict(zip(keys,values))

print (assignment)

#adding values to assignment
assignment[5] = "Location"

print (assignment)

#deleting values from assignment
del assignment [3]

print(assignment)

#prints out keys for assignment dictionary
assignment.keys()
assignment.values()