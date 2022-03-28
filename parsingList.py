def count(lst):

    #odd and even variables start as empty lists
    odd = 0
    even = 0

    #for loop to iterate through lst
    for i in lst:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    
    return even, odd


lst = [1,2,3,4,5,6,7,8,2,3,4,5,6,7,8]
even, odd = count(lst)

print (f"Even : {even}, Odd : {odd}")