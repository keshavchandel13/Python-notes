name="keshav"

nameShort=name[2 : 5] #Using string slice (array slicing)
print(nameShort)
print(name[-4 : -1]) #Using string slice (array slicing) using negative index

#String function

# 1) length of the string
print(len(name))

# 2) Verify the string end with
print(name.endswith("av"))

# 3) Verify the string start with
print(name.startswith("m"))

# 4) To capatlize first letter
print(name.capitalize())

# 5) To upper case 
print(name.upper())

# 6) To replace the string
s="hello world"
replaced=s.replace("world","python")
print(replaced)

