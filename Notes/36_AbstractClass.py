# Abstract: is a process of hiding implementation details and showing only essential features. It allows you to focus on what an object does rather than how it does it
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod 
    def perimeter(self):
        pass
class circle(shape):
    def __init__(self,rad):
        self.radius = rad
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius
c = circle(10)
print(c.area())
print(c.perimeter())
    