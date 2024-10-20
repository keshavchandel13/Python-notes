# Parent class
class Parent:
    def add_numbers(self, num1, num2):
        return num1 + num2
class Child(Parent):
    def add_numbers(self, num1, num2):
        return abs(num1) + abs(num2)

parent_instance = Parent()

child_instance = Child()


parent_addition = parent_instance.add_numbers(-10, 5)  
child_addition = child_instance.add_numbers(-10, 5)   

print(f"Addition with signs (Parent class): {parent_addition}")
print(f"Absolute addition (Child class): {child_addition}")


print("Parent class ")
print(Parent.__dict__)

print("Child class ")
print(Child.__dict__)
