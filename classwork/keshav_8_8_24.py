#PROBLEM 1: print even  numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
'''
numbers = [ 
386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 
626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 
379, 843, 831, 445, 742, 717, 958,743, 527] 

for num in numbers:
 if(num %2==0):
    if(num!=237):
        print(num)
    else:
        break
'''

# PROBLEM :2 Python program that accepts a single integer value entered by the user. If the value entered is less than one, the program prints nothing. If the user enters a positive integer, n, the program prints an n×n box drawn with *
'''
n = int(input("Enter the number between 1 to 9: "))

if n < 1 or n > 9:
    print("Nothing")
else:
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()
'''
                           #PPT PROBLEMS
        #-->>> TUPLE PROBLEMS
#PROBLEM 3: to create a tuple that stores your name, roll number and your gmail ID

'''
name = input("Enter your name: ")
roll = int(input("Enter your roll number: "))
gmail = input("Enter your gmail Id: ")
detail=(name, roll, gmail)
print("Your details are: ",detail)
'''


#PROBLEM 4: Write a program  a tuple whose elements are tuples with other tuples in it.
'''
place=( ("shimla", "Manali", "Kullu"), ("JUIT", "BAHRA", "HPU") )
print("Printing whole tuple",place)
print("Printing index 0 of tuple: ",place[0])
print("Printing index 1 of tuple: ",place[1])
'''


#PROBLEM: 5 Write a program to generate the error TypeError: 'tuple' object does not support item assignment
'''
uni = ("JUIT", "BAHRA", "HPU", "CU", "CGC")
uni[0]="NIT"
'''


# ---->>> LIST problem

# PROBLEM 6: Write a program to illustrate the operation of a stack (LIFO)
'''
mylist = [1,2,3,4,5,6]
mylist.pop()
print(mylist)
'''

#PROBLEM 7: Write a program to show the implementation of a queue (FIFO) 
'''
mylist = [1,2,3,4,5,6]
mylist.remove(mylist[0])
print(mylist)
'''

#PROBLEM 8: list: list1 = ["abc",[2,3,("mohit","the avengers")],1,2,3] Using in operator checkthe presence of the word  avengers in the list. If it is True print it by getting it's index.
'''
list1 = ["abc",[2,3,("mohit","the avengers")],1,2,3]
if("avengers" in list1):
    print(True)
else:
    print(False)
'''

#PROBLEM 9: With the for loop, take the following list and sort it based on the sum of the values of the tuples ofthe list: [(1,5),(9,0),(12,3),(5,4),(13,6),(1,1)
'''
list_of_tuples = [(1, 5), (9, 0), (12, 3), (5, 4), (13, 6), (1, 1)]
sorted_list = []


for i in range(len(list_of_tuples)):
    current_tuple = list_of_tuples[i]
    tuple_sum = current_tuple[0] + current_tuple[1]
    sorted_list.append((tuple_sum, current_tuple))

sorted_list.sort()


sorted_tuples = [t[1] for t in sorted_list]

print(sorted_tuples)
'''

# PROBLEM 10: Use the list, [1,2,4,5,1,1,4,1,56], and find the index of all the 1 elements.
'''
list = [1,2,4,5,1,1,4,1,56]
print(list.index(1))
'''

#PROBLEM 11: Write a program that accepts any number and prints the number of digits in it

num = int(input("Enter the number: "))
count = 0

while num != 0:
    num =num//10 #Used for floor division
    count += 1

print("Number of digits: ", count)


