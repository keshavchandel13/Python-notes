a = int(input("Enter the number of character you want to read from file: "))
with open(file="Data.txt",mode='r') as file:
    content1=file.read(a)
    content2=file.read(2*a)
    content3=file.read(3*a)
    print(content1)
    print(content2)
    print(content3)
