from numpy import *

arr = array([

    [1,2,3,4],
    [5,6,7,8]
])

m = matrix(arr)

print(m)
  

m1 = matrix('1 2 3 4; 5 6 7 8')

print(m1)

m2 = matrix('1 2 3; 6 7 8;2 4 4')
m3 = matrix('1 2 3; 6 7 8; 1 4 7')

m4 = m2 + m3 ;
m4 = m2 * m3;
print(m4)