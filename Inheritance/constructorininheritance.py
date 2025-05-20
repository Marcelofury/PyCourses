class A:
    def __init__(self):  #constructor of A
        print("In A init")
    def formula1(self):
        print("This is formula1")

    def formula2(self):
        print("This is formula2")

class B(A):   #inheritance of A  #Sub/Child Class
    def __init__(self):  #constructor of B
        super().__init__()    #using Super()
        print("In B init")

    def formula3(self):
        print("This is formula3")

    def formula4(self):
        print("This is formula4")


a1 = B()

