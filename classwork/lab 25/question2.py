'''. Write a python function to check whether three given numbers can form the sides of a triangle. Hint:
Three numbers can be the sides of a triangle if none of the numbers are greater than or equal to the
sum of the other two numbers.'''
def checkTriangle(num1,num2,num3):
    if num1>=num2+num3:
        return False
    elif num2>= num1+num3:
        return False
    elif num3>= num1+num2:
        return False
    else:
        return True
num1 = int(input("Enter the number1:"))
num2 = int(input("Enter the number2:"))
num3 = int(input("Enter the number3:"))
if checkTriangle(num1,num2,num3):
    print("Triangle can be formed")
else:
    print("Can't form triangle")
