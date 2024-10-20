fileloc=r"C:\Python\Problem\replace.txt"
'''''
word="donkey"
with open(fileloc,"r") as f:
    content=f.read()
contentNew=content.replace("donkey","#####")
with open(fileloc,"w") as f:
    f.write(contentNew)
'''

#for list of words
words = ["donkey", "bad", "bitch"]

with open(fileloc,"r") as f:
    content=f.read()
for word in words:
    content=content.replace(word,"censored")
with open(fileloc,"w") as f:
    f.write(content)