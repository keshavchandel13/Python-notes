class employee:
    a=1

    @classmethod
    def show(cls):
        print(f"The value of the a is {cls.a}")
    @property 
    def name(self):
        return f"First name: {self.fname}\n last name: {self.lname}"
    @name.setter
    def name (self,value):
        self.fname =value.split(" ")[0]
        self.lname =value.split(" ")[1]
    @staticmethod
    def greet():
        print("Hello sir")

e = employee()
e.a=45
e.greet()
e.name = "Keshav chandel"
print(e.name)
e.show()



