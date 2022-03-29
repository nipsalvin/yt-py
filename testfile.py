def count(lst):
    more = [""]
    less = [""]

    for i in lst:
        if len(i) <= 5:
            print(f'{i} is less')
        else:
            print(f'{i} is more')
    

lst = ["Alvin", "Nips", "Pips-by-Nips"]


count(lst)
