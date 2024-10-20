import time

# Recursive factorial function
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Iterative factorial function (non-recursive)
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = 5
s_time_recursive = time.time()
factorial_recursive(num)
e_time_recursive = time.time()

s_time_iterative = time.time()
factorial_iterative(num)
e_time_iterative = time.time()

final_time_recursive = e_time_recursive - s_time_recursive
final_time_iterative = e_time_iterative - s_time_iterative

# Corrected print statements
print("Time taken by recursive: %.10f" % final_time_recursive)
print("Time taken by iterative: %.10f" % final_time_iterative)
