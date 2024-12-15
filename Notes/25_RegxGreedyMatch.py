import re
text = 'My name is keshav. My full name is keshav Chandel , keshavkeshav'
y = re.findall('(keshav)+',text)
print(y)