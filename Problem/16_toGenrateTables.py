fileloc=r"C:\Python\Problem\tables"
def genrateTable(n):
    table=""
    for i in range (1,11):
        table+=f"{n} X {i} = {n*i}\n"
    with open(fileloc + f"/table{n}.txt","w") as f:
        f.write(table)
    





for i in range (2,21):
    genrateTable(i)