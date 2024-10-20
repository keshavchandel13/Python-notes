#function
'''
def sum():
    a=int(input("Enter the first number "))
    b=int(input('Enter the second number '))
    return a+b
result=sum()
print(result)
'''

#recursion
'''
def fact(n):
    if(n<1):
      return 1
    else:
       return n*fact(n-1)
      

a=int(input("Enter the number: "))
print(fact(a)) 
'''

#Greatest of three number using function
'''
def great(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a  and b>c):
        return b
    else:
        return c
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
ans=great(a,b,c)
print(f"The greatest number in {a},{b},{c} is {ans}")
'''

#sum of the natural number using recursion
'''
def sumOfnaural(num):
    if(num==1):
     return 1
    else:
       return num+sumOfnaural(num-1)
a=int(input("Enter the number "))
print(f"The sum of first {a} natural number is {sumOfnaural(a)}")
'''
#Inch to cenimeter using function
'''
def inchtocem(n):
    return n*2.54
n=int(input("Enter the inches "))
print("Ans: ",inchtocem(n))
'''

#To remove the word from the list
'''
list=["keshav","sai","rahul","rohit","nitin","ankit"]
def rem(word):
    return list.remove(word)
word=input("Enter the word: ")
rem(word)
print(list)
'''