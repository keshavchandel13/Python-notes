name=input("Enter your name ")
print(f"Good afternoon {name}") #first method
print("Good afternoon "+name) #second method
print("Good afternoon ",name) #Third method
# Fifth method using format method
print("Good afternoon {}".format(name))

# Sixth method using % operator
print("Good afternoon %s" % name)

# Seventh method using join method
print("".join(["Good afternoon ", name]))