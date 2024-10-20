path = r"C:\Python\p1 exam\dataQues1.txt"
def assign_grade(total_marks):
    if total_marks >= 80:
        return "A+"
    elif 70 <= total_marks < 80:
        return "A"
    elif 60 <= total_marks < 70:
        return "B+"
    elif 50 <= total_marks < 60:
        return "B"
    else:
        return "F"

name = []
roll = []
total_marks = []
grades = []

with open(path, 'r') as f:
    for line in f:
        data = line.split('-')
        print(data)
        name.append(data[0])
        roll.append(data[1])
        marks = int(data[2].strip())
        total_marks.append(marks)
        grades.append(assign_grade(marks))  

for i in range(len(name)):
    print(f"Name: {name[i]}, Roll No: {roll[i]}, Total Marks: {total_marks[i]}, Grade: {grades[i]}")
