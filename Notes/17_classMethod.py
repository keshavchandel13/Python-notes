class employee:
    a=1
    def display(self):
        print(f"The value of the a is {self.a}")
        
    @classmethod
    def show(cls):
        print(f"The value of the a is {cls.a}")
e = employee()
e.show()
employee.a=45
employee.show() #here if we haven't used the classmethod it will show the output 4 but we have used classmethod it with directly access the class irrespective of object.

