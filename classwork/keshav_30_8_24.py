#find  the sum of the squares of first n integers
'''
n = int(input("Enter the value of n: "))
def sum_of_square(n):
    sum = 0
    for i in range(1,n+1):
        
        sum = sum + i*i
    return sum
print(sum_of_square(n))

'''
#find  the sum of the squares of first n integers---> Recursion
'''
n = int(input("Enter the value of n: "))
def sum_of_square(n):
    if  n==1:
        return 1
    else:
        return sum_of_square(n-1)+ n*n
print(sum_of_square(n))
'''

#Problem:3
# ∗ Generate the large list of integers ( original list) using random module.
import random
list=[]
n = int(input("Enter the size of the list: "))
for i in range(0,n):
  list.append(int(random.random()*10))
print(list)

# Slicing of list:
start = int(input("Enter the starting point of the slicing: "))
end = int(input("Enter the end point of the slicing: "))
if start>0 and end<int(len(list)):
  print(list[start:end])