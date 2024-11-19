'''. You have x no. of 5 rupee coins and y no. of 1 rupee coins. You want to purchase an item for amount z.
The shopkeeper wants you to provide exact change. You want to pay using minimum number of coins.
How many 5 rupee coins and 1 rupee coins will you use? If exact change is not possible then display -1.'''
def balance(fiveCoin,oneCoin,amount):
    five_rupee_coin = min(amount//fiveCoin,fiveCoin)
    remaining_amount = amount - five_rupee_coin * 5
    if remaining_amount <= oneCoin:
         return five_rupee_coin, remaining_amount
    else:
         return -1

fiveCoin = int(input("Enter the number of five coin:"))
oneCoin = int(input("Enter the number of one coin:"))
amount = int(input("Enter the amount:"))
result = balance(fiveCoin, oneCoin,amount )
if result == -1:
     print("Exact change is not possible")
else:
     print(f"Use {result[0]} five rupee coins and {result[1]} one rupee coins")