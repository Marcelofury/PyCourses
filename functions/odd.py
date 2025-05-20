def count(lst) :
    even = 0
    odd = 0

    for i in lst:
        if i%2==0:
            even+=1
        
        else:
            odd+=1

    return even,odd

lst = [1,4,3,5,7,89,54,31,67,23]

even,odd = count(lst)

print(even)
print(odd)

print("Even : {} and odd : {}".format(even,odd))