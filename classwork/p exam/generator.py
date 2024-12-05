def generator_fun():
    x=3
    for i in range(1,7):
     yield pow(x,i)

for value in generator_fun():
    print(value)
#----------Using loops
print("\nUsing the loops\n")
x = 3
for i in range(1,7):
    print(pow(3,i))