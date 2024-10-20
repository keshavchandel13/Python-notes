import random
n  = random.randint(1,1000)
attempt=1
choice=-1
print("*********WELCOME TO GUESS NUMBER************")
while(choice!=n):
    choice = int(input("Guess the number number between 1 to 1000: "))
    if(choice>n):
        print("Enter less number")
        attempt+=1
    elif(choice<n):
        print("Enter the larger number")
        attempt+=1
print("\n\nCongratulation!")
print(f"You guessed right  number {n} in {attempt} attempts")