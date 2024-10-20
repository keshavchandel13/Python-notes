class Student:
    institution = "JUIT"
    def __init__(self,student_name,batch):
        self.student_name = student_name
        self.batch = batch
    def create_email(self):
        return self.student_name + self.batch + "@" + self.institution + ".ac.in"
s1 = Student('Keshav', "A19")
s2 = Student('Anshit', "A19")
s3 = Student('Rajat', "A19")

print("Detail Of the student: ") 
print(s1.student_name,s1.batch,s1.institution,s1.create_email())
print(s2.student_name,s2.batch,s2.institution,s2.create_email())
print(s3.student_name,s3.batch,s3.institution,s3.create_email())

# Changing institution name 
s2.institution="HPU"
print("\nDetail of student after changing institute name: ")
print(s1.student_name,s1.batch,s1.institution,s1.create_email())
print(s2.student_name,s2.batch,s2.institution,s2.create_email())
print(s3.student_name,s3.batch,s3.institution,s3.create_email())



        