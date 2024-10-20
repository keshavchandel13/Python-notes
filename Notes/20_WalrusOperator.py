#Use of walrus operator:
'''
if(n:= len([1,2,3,4,5])) >3:
    print(f"List is too long {n} elements, expected <=3")
'''

#Type defination
'''
n : int=5 #It shows the n variable is int type
name : str ="Keshav" #it shows thw name variable is of string type

def sum(a:int, b:int)->int: #it shows that function return integer tyepe
    return a+b;
'''

#Match case: Similar to the switch statement:
'''
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "NOT FOUND"
        case 500:
            return "Internal server error"
        case _:
            return "Unknown status"
print(http_status(405))
'''



