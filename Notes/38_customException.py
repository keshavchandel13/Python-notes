class meraError(Exception):
    def __init__(self,m):
        super().__init__(m)
try:
    name = input("Enter your name: ")
    if name == "shivam":
        raise meraError("ye ganda hi banda hai")
except meraError as e:
    print(e)
