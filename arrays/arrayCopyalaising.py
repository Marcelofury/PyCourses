from numpy import *

arr = array([1,2,4,4,5,3])
arr1 = arr  # copies arr into arr1

print(arr1)

print(id(arr1))
print(id(arr))   #same id = aliasing