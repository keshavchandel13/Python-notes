'''Write a python program to find and display the product of three positive integer values based on the rule
mentioned below: It should display the product of the three values except when one of the integer value
is 7. In that case, 7 should not be included in the product and the values to its left also should not be
included. If there is only one value to be considered, display that value itself. If no values can be
included in the product, display -1. Note: Assume that if 7 is one of the positive integer values, then it will
occur only once.'''

def product(values):
    if 7 in values:
        index = values.index(7)
        values = values[index+1:]
    if len(values)==0:
        return -1
    result = 1
    for val in values:
        result *= val
    return result 
num1 = int(input("Enter the number1:"))
num2 = int(input("Enter the number2:"))
num3 = int(input("Enter the number3:"))
values = [num1,num2,num3]
ans = product(values)
print("The product is: ",ans)