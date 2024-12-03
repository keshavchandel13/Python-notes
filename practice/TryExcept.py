try:
    b=2/0
    print(b)
except ZeroDivisionError:
    print("Error: Dividing with zero")
else:
    print("hillooo")
finally:
    print("Jai ho")
