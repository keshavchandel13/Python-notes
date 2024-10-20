# Super() method is used when inherited class also wants the access of the consturctor of the base class

class employee:
    def __init__(self):
        print("It is the constructor of the employee")
class code(employee):
    def __init__(self):
        print("it is the constructor of the code")
class programmer(code):
    def __init__(self):
        super().__init__() # with super() we can call the constructor of the base class
        print("It is the constructor of the programmer")
keshav = programmer()
