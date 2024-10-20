str = "mississippi"
lst = []
lst2 = []
for ch in str:
    if ch in lst:
        pass
    else:
        lst.append(ch)
        lst2.append(ch)
newstr = ''.join(lst2)
print(newstr)