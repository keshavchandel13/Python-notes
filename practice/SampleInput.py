with open(file="SP1.txt",mode='w') as f1:
    f1.write("Name: ABC\n")
    f1.write("Batch:CS12\n")
    f1.write("Roll No:123\n")
with open(file="SP2.txt",mode='w') as f2:
    f2.write("City:PQR\n")
    f2.write("District:LMN\n")
    f2.write("State:XYZ\n")
with open(file="Combined.txt",mode='w') as combine:
    with open(file="SP1.txt",mode='r') as f1:
        for line in f1:
            combine.write(line)
    with open(file="SP2.txt",mode='r') as f2:
        for line in f2:
            combine.write(line)