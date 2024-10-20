class programmer:
    name=""
    salary=0
    dept=""
    def __init__(self):
        self.name=input("Enter your name ")
        self.salary=int(input("Enter your salary "))
        self.dept=input("Enter your department ")
    def display(self):
        print(f"The employee name is {self.name}\n The salary of the employee is {self.salary}\n The dept of the employee is {self.dept}\n\n\n")
keshav = programmer()
shivam = programmer()
om = programmer()
keshav.display()
shivam.display()
om.display()
