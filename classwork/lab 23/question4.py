'''
Write a Python program to create a generator function that generates the powers of a number up
to a specied exponent. Do the same using a loop. Observe the dierence between the two
'''
def generator_fun():
    for i in range(1,7):
     yield pow(2,i)

for value in generator_fun():
    print(value)
#----------Using loops
print("\nUsing the loops\n")
for i in range(1,7):
    print(pow(2,i))

