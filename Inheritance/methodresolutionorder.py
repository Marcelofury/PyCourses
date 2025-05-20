class A:        
    def __init__(self):
        print("In A init")                   
    def formula1(self):
        print("This is formula1")

    def formula2(self):
        print("This is formula2")

class B():   
    def __init__(self):
        print("In B init")   
    def formula3(self):
        print("This is formula3")

    def formula4(self):
        print("This is formula4")


class C(A,B): 
    def __init__(self):
        super().__init__() #this prints A and C thus mrthod resolution order
        print("In C init")   
    def formula5(self):
        print("This is formula5")

    def formula6(self):
        print("This is formula6")

a1 = C()




