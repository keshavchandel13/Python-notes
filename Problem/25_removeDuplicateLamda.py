
lst1 = [1,2,3,4,5,6,7,8,9,10]
lst2 = [2,4,6,8]

lst3 = list(filter(lambda x:x not in lst2,lst1))
print(lst3)