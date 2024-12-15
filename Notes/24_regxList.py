import re
x = 'HELLO TO EVERYONE THUS IS TEST FOR AEIOU'
y = re.findall('[AEIOU]+',x)
print(y)

x = 'my 2 fav number is 19 and 42'
y = re.findall('[0-9]',x)
print(y)