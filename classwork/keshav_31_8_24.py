def fun(x):
    return (x**3 - x - 1)

# S1:
accuracy = 0.2
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
value_a = fun(a)
value_b = fun(b)

if value_a * value_b < 0:
    # S2: 
    while True:
        # S3:
        mid = (a + b) / 2
        mid_value = fun(mid)
        
        if mid_value == 0 or abs(b - a) < accuracy:
            print(f"{mid} is the root within the desired accuracy")
            break
        elif fun(a) * mid_value < 0:
            b = mid
        else:
            a = mid
else:
    print("The function does not have a root in the given interval")
