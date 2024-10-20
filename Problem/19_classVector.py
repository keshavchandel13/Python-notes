# Problem:1 Create a class (2-d vector) and use it to create another class reoresenting 3-d vector
'''
class TwoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The dimension of the 2-d vector is: {self.i}i + {self.j}j")
class ThreeDVector(TwoDVector):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.k = k
    def show(self):
        print(f"The dimension of the 2-d vector is: {self.i}i + {self.j}j + {self.k}k")
o1 = TwoDVector(2,3)
o1.show()

o2 = ThreeDVector(4,5,6)
o2.show()
'''

#PRoblem: 2 Create a class 'pets' from a class 'Animals' and further create a class 'Dog' from 'Pets'. And a method 'Bark' to class "dog"
'''
class Animals:
    pass
class Pets(Animals):
    pass
class Dog(Pets):
    @staticmethod
    def bow():
        print("bark bow bow!")
Dog.bow()
'''

#PROBLEM:3 Create a class 'Employee' and add increment properties to it

class Employee:
    salary = 2000
    increment = 20
    @property
    def salaryAfterIncrement(self):
        return self.salary+ self.salary*(self.increment/100)
    @salaryAfterIncrement.setter 
    def salaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary)-1)*100

e = Employee()

e.salaryAfterIncrement = 2400
print(e.increment)