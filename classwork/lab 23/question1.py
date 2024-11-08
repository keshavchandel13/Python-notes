# # Iterator

# a=-10
# b=a.__abs__()
# # print(next(a))
# lst=[1,2,3,4]
# itr_for_lst=iter(lst)
# print(type(itr_for_lst))
# print(itr_for_lst)
# print(dir(a))
# print("list function:")
# print(dir(lst))
# print(b)

# s="abc"
# print("\nfunction for string\n\n")
# print(dir(s))
# iter_s2=iter(s)
# print(iter_s2)
# for char in iter(iter_s2):
#     print(char) 

# dict={
#     "car":"alto 800",
#     "model":2018
# }
# print(type(dict))
# print(dir(dict))
# itr_dict=iter(dict)
# print(next(itr_dict))
# print(next(itr_dict))

#Q--> Write few lines of code to observe that iterators are ALSO iterable
'''
lst = [1,2,3,4]
itr_lst = iter(lst)
iterator = iter(itr_lst)
for x in iterator:
    print(x)
'''
# lst = [1,2,3,4]
# itr_lst = iter(lst)
# while True:
#     try:
#       print(next(itr_lst))
#     except:
#       break


def my_range_yield(a,b):
    x1 = range(a, b)
    for x in x1:
        yield x    
x2= my_range_yield(8,12)
for i in x2:
    print(i)



