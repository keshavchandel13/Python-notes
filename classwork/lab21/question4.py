class First:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        return self.a+self.b
class Second:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def subtract(self):
        return self.a-self.b
class Third(First,Second):
    def __init__(self, a, b):
        super().__init__(a, b)
obj1 = Third(2,5)
print(f"The sum of the two number is: {obj1.sum()}\nThe subtraction of two number is: {obj1.subtract()}")

