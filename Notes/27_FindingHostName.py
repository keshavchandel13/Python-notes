import re
text = 'From: chandelkeshav4@gmail.com at 9:30 am'
start_pos = text.find('@')
print(start_pos)
end_pos = text.find(" ",start_pos)
print(end_pos)
domain = text[start_pos+1:end_pos]
print(domain)