list_names = []
def func(list_names):
    n = int(input("Enter the lenght of the list: "))
    for i in range (1,n+1):
        names = input("Enter the names: ")
        list_names.append(names)
    print("Here the list of names:", list_names)
    more_five =[]
    less_five = []
    for k in list_names:
        if len(k)>=5:
            more_five.append(k)
        else:
            less_five.append(k)
    print(f"five letters and above {more_five}\nless than five letters {less_five} ")

func(list_names)