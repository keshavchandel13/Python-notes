try:
    if a > 0: 
        print("jai ho")
    k="hello"
    print(int(k))
except NameError:  
    print("There is name error")
except ValueError: #this will be skip 
    print("There is value error")
finally:
    print("Mai bahar hu")  