#Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
'''
def sum_two_integers(a, b):
    total = a + b
    if total>=15 and total<=20:
        return 20
    else:
        return total


num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
result = sum_two_integers(num1, num2)
print("The answer is:", result)
'''
#Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.

principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (as a percentage): "))
num_years = int(input("Enter the number of years: "))

future_value = principal_amount * ((1 + (rate_of_interest / 100)) ** num_years)


print(f"The future value of the investment is: {future_value:.2f}")
print(f"Amount:    {principal_amount:.2f}")
print(f"Interest:    {future_value-principal_amount:.2f}")
print(f"Total:     {future_value:.2f}")
