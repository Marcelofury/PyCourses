evens = [2,3,6,8,7,2,4,8,9,1]

evens = list(filter(lambda n : n%2==0,evens))

doubles = list(map(lambda n : n*2,evens))

print(evens)
print(doubles)