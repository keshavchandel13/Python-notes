a=(1,2,3,"keshav","rohan",1.2);
print(type(a)); #This is of type class: tuple

#a[0]=3; #this will give a error because tuple is immutable

b=(1,)# single element tuple
print(type(b));

#Concatenation:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
new_tuple = tuple1 + tuple2
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6)

#Repetition:
my_tuple = (1, 2, 3)
repeated_tuple = my_tuple * 3
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
