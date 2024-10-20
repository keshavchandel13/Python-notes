n1 = int(input("ENter the number one: "))
n2 = int (input("Enter the second number: "))
if(n2==0):
    raise ZeroDivisionError("Cann't divide with zero")
else:
    print(n1/n2)