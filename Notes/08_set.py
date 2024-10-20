#set: Collection of well defined object
# To create a empty set
# Syntax
#a=set();

a={22,34,1,34,1,1,1,23};# simple set
print(a);# doesn't repeat the values 
# doesn't follow order

#Methods in the SET
c={12,55,23,13,57}
d={23,88,53,95,33}
print(c.union(d));
print(c.intersection(d));