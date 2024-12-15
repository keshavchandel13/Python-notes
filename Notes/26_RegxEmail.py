import re
text = 'From: chandelkeshav4@gmail.com at 9:30 am'
y = re.findall(r'\S+@\S+\.\S+',text)
print(y)