class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    @property
    def email(self):
       
        return f"{self.name}{self.roll}@juit.ac.in"

    @staticmethod
    def college():

        return "JUIT"
s1 = Student("Keshav",231030313)
print(s1.email)
print(Student.college)
