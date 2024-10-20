#problem: 1 find the greatest number in four number
'''
a=int(input("Enter the first number: "));
b=int(input("Enter the second number: "));
c=int(input("Enter the third number: "));
d=int(input("Enter the fourth number: "));

if (a>b and a>c and a>d):
    print("A is greatest")
elif (b>a and b>c and b>d):
   print("B is greatest")
elif (c>a and c>b and c>d):
   print("C is greatest")
else:
   print("D is greatest")
'''

#Problem:2 student is passed or failed
physics=float(input("Enter the marks of the physics: "))
maths=float(input("enter the marks of maths: "))
chemistry=float(input("enter the marks of the chemistry: "))
s=physics+maths+chemistry
percent=100*(s/300)

if (percent>=33 and physics>=33 and chemistry>=33 and maths>=33):
    print("You passed exam")
else:
    print("You failed")
