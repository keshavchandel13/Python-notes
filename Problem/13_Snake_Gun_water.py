import random
pt_user = 0
pt_comp = 0
counter = 0

def game(user_choice, rounds):
    global pt_user, pt_comp, counter
    compChoice = random.randrange(0, 3)
    # print(compChoice)
    if counter != rounds:
        counter += 1
        if (compChoice == 0 and user_choice == "s") or (compChoice == 1 and user_choice == "w") or (compChoice == 2 and user_choice == "g"):  # 0 for snake, 1 for water, 2 for gun
            print("Draw")
        elif compChoice == 0 and user_choice == "w":
            print("You lost")
            pt_comp += 1
        elif compChoice == 1 and user_choice == "s":
            print("You won")
            pt_user += 1
        elif compChoice == 1 and user_choice == "g":
            print("You lost")
            pt_comp += 1
        elif compChoice == 2 and user_choice == "s":
            print("You lost")
            pt_comp += 1
        elif compChoice == 0 and user_choice == "g":
            print("You won")
            pt_user += 1
        else:
            print("You won")
            pt_user += 1
    if(counter==rounds):
        if(pt_user>pt_comp):
            print("You won this match")
        else:
            print("You lost this game, try again later")
print("**************WELCOME TO SNAKE GUN WATER GAME****************")
rounds = int(input("Enter the number of rounds you want to play: "))
i = 0
while i < rounds:
    user_choice = input("Enter 'S' for snake 'W' for water 'G' for gun\n").lower()
    game(user_choice, rounds)
    i+=1
