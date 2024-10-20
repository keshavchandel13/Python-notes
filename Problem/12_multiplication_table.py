#Multiplication table 
'''
num=int(input("Enter the number: "))
for i in range(1,11):
    print(f"{num} X {i} = ",num*i)
'''

#TO GREET A PERSON WHOOSE NAME START WITH s
''''
names=["Keshav","shivam","sai","rohan","shivang"]
for i in names:
    if(i.lower().startswith("s")):
        print(f"Hello {i}")
'''
#Problem 1: whith while loop
'''
num=int(input("Enter the number: "))
i=1
while (i<=10):
    print(f"{num} X {i}=",num*i)
    i+=1
'''

#Number is prime
''' 
num=int(input("Enter the number: "))
for i in range(2,num):
    if(num%i==0):
        print("Number is not prime")
        break
else:
    print("Number is prime")
'''
#Sum of the first natural number
'''
n=int(input("Enter the number: "))
i=1
sum=0
while i<n+1:
    sum+=i
    i+=1
print(f"The sumof the first {n} natural number is: ",sum)
'''

#Factorial of the number
'''
n=int(input("Enter the numebr: "))
fact=1
for i in range(n,0,-1):
    fact=fact*i
print("the factorial is: ",fact)
'''

# Star pattern
