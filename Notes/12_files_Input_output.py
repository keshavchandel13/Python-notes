# input output of files in python
path = r"C:\Python\Notes\test.txt"
# TO read a file
'''
file=open(path) #By default the mode is read
data = file.read()
print(data)
file.close()
'''

# To write a file
'''
file=open(path,"a")
data="i am adding these lines to the file"
file.write(data)
file.close()
'''

# Readlines function: function used to read line by line
"""""
file=open("test2.txt")
data= file.readlines()
print(data, type(data))
file.close()
"""""

# If we want to  get rid of close() we can use
# with open("test2.txt") as f:
#     print(f.read())
