#Encapsulation is the process of bundling data (variables) and methods (functions) that operate on that data into a single unit, i.e., a class.

# Data Hiding is a part of encapsulation where access to internal data is restricted to prevent accidental modification.

class student:
    def __init__(self,name,age):
        self.__name = name #private data memeber
        self._age = age #protected member
    def getAge(self):
        return self.__age
keshav = student("Keshav",19)
print(keshav.getAge())
        