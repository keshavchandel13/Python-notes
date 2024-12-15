import re
text = 'From: chandelkeshav4@gmail.com at 9:30 am'
y = re.findall(r'@([^ ]*)',text)
print(y)