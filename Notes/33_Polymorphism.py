# Polymorphism
class kutta:
    def speak(self):
        print("Bhonk")
class billi:
    def speak(self):
        print("meow")
animals = [kutta(),billi()]
for i in animals:
    i.speak()