class employee:
    a=1

    @classmethod
    def show(cls):
        print(f"The value of the a is {cls.a}")
e = employee()
e.a=45
e.show() #here if we haven't used the classmethod it will show the output 4 but we have used classmethod it with directly access the class irrespective of object.

