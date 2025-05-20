class A:                           
    def formula1(self):
        print("This is formula1")

    def formula2(self):
        print("This is formula2")

class B():   
    def formula3(self):
        print("This is formula3")

    def formula4(self):
        print("This is formula4")


class C(A,B):   #inheritance of C from A and B  #Sub/Child Class of A and B
    def formula5(self):
        print("This is formula5")

    def formula6(self):
        print("This is formula6")

a1 = A()

a1.formula1()
a1.formula2()

b1 = B()


b1.formula3()
b1.formula4()

c1 = C()
c1.formula1()
c1.formula2()
c1.formula3()
c1.formula4()
c1.formula5()
c1.formula6()
