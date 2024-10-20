class Student:
    def __init__(self,n,r):
        self.name = n
        self.roll = r
    def email_gen(self):
        name = (self.name).replace(" ","")
        return  name+str(self.roll)+"@juit.ac.in"
    def email_instance(self):
        name = (self.name).replace(" ","")
        return  name+str(self.roll)+"@juit.ac.in"
        
s1 = Student("Keshav Chandel",231030313)
s2 = Student("Rajat Rajput",231030246)

print(f"Details  of s1 student:\nName: {s1.name}\nRollNo: {s1.roll}\nEmail: {s1.email_gen()}\n")
print(f"Details  of s2 student:\nName: {s2.name}\nRollNo: {s2.roll}\nEmail: {s2.email_gen()}\n")

s3 = Student("Anshit pandit",23130255)

print(Student.email_instance(s3)) #Instance function called
