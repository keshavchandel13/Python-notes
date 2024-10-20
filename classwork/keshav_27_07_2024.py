#Day: 2 of python coding

#Format Specifier
'''
pi=3.14159265
print("The value of the PI is:",pi)
print("The value of the PI is:%d "%pi)
print("The value of the PI is:%f "%pi)
print("The value of the PI is:%lf "%pi)
print("The value of the PI is:%10.3f" %pi)
'''

#format specifier
'''
a=input("Enter the value of the a ")
b=input("Enter the value of the b ")
if a>b: 
    print("A is greater then B")
elif a<b: #else if conditon written in python as elif
    print("B is greater then A")
else:
    print("A and B is equal")
'''

#Variable
city="Hamirpur"
'''
print(id(city))#id(variable_Name) is used to get the id of the variable
print(type(city))#type(variable_Name) is used to get type of variable
'''

#complex numbers
'''
x=complex(2,5)
print("The complex number is: ",x)
'''
#ASCII code
'''
x="Q"
print(ord(x))
#ASCII code to Char
x=82
print(chr(x))

'''

#BITWISE OPERATOR
a = 10
b = 4


print("The value of n1 in decimal is:\t%d"%a,'\n')
print("The value of n1(%d)"%a,"in binary is ",f'0b{a:08b}','\n')
print("The value of n1 in decimal is:\t%f"%b,'\n')
print("The value of n1(%d)"%b,"in binary is ",f'0b{b:08b}','\n')

#AND Operator(&)
c=a&b;
print("a & b =%d" %c)

#OR Operator(|)
c=a|b
print("a|b: %d"%c)

#XOR Operator(~)
c=~a
print("a~b: %d"%c)

#One's Complement Operator(^)
c=a^b
print("a^b: %d"%c)
