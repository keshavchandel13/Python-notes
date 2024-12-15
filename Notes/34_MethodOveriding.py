class Parent:
    def greet(self):
        return "Hello from Parent class"
class bacha(Parent):
    def greet(self):
        return "Hello from bacha class"
obj = bacha()
print(obj.greet())