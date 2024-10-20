class employee: #base class or parent class
    company="Google"
    name=None
    salary=None
    def detail(self):
        print(f"The name of the employee is: {self.name}\nThe salary of the employee is: {self.salary} ")
    def getData(self):
        self.name=input("Enter your name: ")
        self.salary=int(input("Enter your salary "))


class programmer(employee): #This is inherited class 
    company="ITC"

# keshav = employee()
# keshav.getData()
# keshav.detail()

shivam = programmer()
shivam.getData()
shivam.detail()
print(shivam.company)