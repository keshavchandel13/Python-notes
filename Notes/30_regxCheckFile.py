import re
line_count=0
upper_count =0
lower_count =0
with open('test3.txt','r') as  file:
    data = file.read()
    print(data)
    upper_count = len(re.findall('[A-Z]',data))
    lower_count = len(re.findall('[a-z]',data))
    for line in data.splitlines():
        if re.match('^[ABC]',line):
            line_count+=1
print(upper_count)
print(lower_count)
print(line_count)
