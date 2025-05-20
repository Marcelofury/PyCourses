class A:                           #Parent Class
    def formula1(self):
        print("This is formula1")

    def formula2(self):
        print("This is formula2")

class B(A):   #inheritance of A  #Sub/Child Class
    def formula3(self):
        print("This is formula3")

    def formula4(self):
        print("This is formula4")


a1 = A()

a1.formula1()
a1.formula2()

b1 = B()

b1.formula1() #result of Inheritance
b1.formula2() #result of Inheritance
b1.formula3()
b1.formula4()