class student:
    def __init__(self):
        pass
s1 = student()
s2 = student()
s1.name = "Keshav Chandel"
s1.roll = 231030313
s1.batch = "A19"

s2.name = "Arjun"
s2.roll = 231030319
s2.batch = "A19"

print(f"Details  of s1 student:\nName: {s1.name}\nRollNo: {s1.roll}\nBatch: {s1.batch}")
print(f"\nDetails  of s2 student:\nName: {s2.name}\nRollNo: {s2.roll}\nBatch: {s2.batch}")