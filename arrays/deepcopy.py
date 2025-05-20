from numpy import *

arr = array([1,2,4,4,5,3])
arr1 = arr.copy() # copies arr into arr1

arr[3] = 7  # even when value changed copies the different value hence deep copy

print(arr)
print(arr1)

print(id(arr1))
print(id(arr))   #different id = deep copy