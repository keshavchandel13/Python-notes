#Dictonary: Used to store collection of the key value pairs
a={
    "Keshav":90,
    "Shivam":100,
    "Om":77
}
print(a, type(a))

#TO print all keys and their values
print(a.items());

#To print all keys in the dictionary
print(a.keys())

#To print values of the key
print(a.values());

#to update the dictionary
a.update({"Shivam":99});
print(a)
a.update({"Parth":69});
print(a);

#to get value at particular key
print(a.get("Keshav"))