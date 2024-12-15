import re
with open('test.txt','r') as file:
    # print(file.read())
    for text in file:
        text = text.rstrip()
        if re.search('^keshav',text):
            print("we found") 