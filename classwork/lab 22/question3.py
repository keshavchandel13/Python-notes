import operator
class Univ_Emp():
    def __init__(self,name,emp_id ,pay):
        self.name = name
        self.id = emp_id
        self.pay = pay
    def __add__(emp1,emp2):
        Univ_Emp.totalSalary = emp1.pay + emp2.pay
        return Univ_Emp.totalSalary
    def __gt__(self,emp2):
        if self.pay>emp2.pay:
            return True
        else:
            return False
emp1 = Univ_Emp("keshav",22333,20000) 
emp2 = Univ_Emp("Rahul",88333,60000)

total = emp1 + emp2

if emp1>emp2:
    print("Keshav salary is more")
else:
     print("Rahul salary is more")




        