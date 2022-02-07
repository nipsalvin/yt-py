nums = [12, 11, 202, 18, 21, 26]

for num in nums:

    if num % 5 == 0:
        print (num)
        #break breaks the iteration once the first value is fetch and doesn't fetch the second value
        break
else:
        print("Not found")

#if you put else under the 'if' block it prints 6 times
#if you put else under 'for' block it prints once after the break



