# Getters: Used to access private variables.
# Setters: Used to modify private variables.
class Student:
    def __init__(self, name, age):
        self.__name = name  # Private variable
        self.__age = age    # Private variable
    @property
    def age(self):
        return self.__name
    @age.setter
    def age(self,age):
        if age>=0:
            print("welcome")
        else:
            print("age must be postive")
    

student = Student("Keshav", 20)
print(student.age)       # ✅ Calls the getter
student.age = 25         # ✅ Calls the setter
print(student.age)       # ✅ Prints updated age
student.age = -5         # ❌ Invalid age, message printed
