a="This is without double space"
print(a.find("  "))

b="This is with double  space"
print(b.find("  "))

#replacing the double space into single space
b=b.replace( "  " , " " ) #strings are imbutable which means that you can not change them by running function
print(b.find("  "))  #in simple words if i have not assigned the value replace to b and just print b.replace it will not change parent string
