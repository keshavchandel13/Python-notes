class unv_employee:
    emp_count = 0
    def __init__(self,f_name,l_name,pay):
        unv_employee.emp_count+=1
        self.f_name = f_name
        self.l_name = l_name
        self.pay = pay
    def create_email(self):
        self.emailId = self.f_name + self.l_name + "@juitsolan.in"
    def display(self):
        print(f"The name of the employee is : {self.f_name} {self.l_name}")
        print(f"The salary of the employee is: {self.pay}")
        print(f"The number of the employee is: {unv_employee.emp_count}")
        print(f"The email id  of the employee is: {self.emailId}")
    def num_emp(self):
        return unv_employee.emp_count
class Instructor(unv_employee):
    instructor_count=0
    def __init__(self, f_name, l_name, pay,sub=None):
        super().__init__(f_name, l_name, pay)
        Instructor.instructor_count += 1
        self.sub1, self.sub2 = (sub[0], sub[1]) if sub and len(sub) >= 2 else (None, None)
    def num_instructor(self):
        return Instructor.instructor_count
emp1 = Instructor("Keshav","Chandel",20000,["Maths","Physics"]) 
emp1.create_email()

emp2 = Instructor("Raju","Thakur",30000,["Computer","English"]) 
emp2.create_email()

emp3 = Instructor("Raman","kumar",6000)



print(f"The number of the employee is {emp2.num_emp()}\nThe number of the instructor is {emp2.num_instructor()}")
print()
# help(Instructor)

print(f"Name:{emp1.f_name} {emp1.l_name}\nSubjects\nSubject1:{emp1.sub1}, Subject2:{emp1.sub2}\n")
print(f"Name:{emp2.f_name} {emp2.l_name}\nSubjects\nSubject1:{emp2.sub1}, Subject2:{emp2.sub2} ")