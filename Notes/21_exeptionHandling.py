try:
    a = int(input("Enter the nummber: "))
    print(a)
except Exception as e:
    print(f"Enter the valid input.\n{e} is not valid input ")