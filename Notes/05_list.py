#Lists are used to store multiple items in a single variable.
items=["PEN",101,"Maxwriter","10.50"];
print(items);
print(items[2]);
print(items[1:3]);

items.append("This is list");
print(items);

num=[1,4,2,88,44,64,34,55];
num.sort();
print(num);
num.reverse();
print(num);
#reverse a list
num=[1,4,2,88,44,64,34,55];
for i in range (len(num)-1,-1,-1):
    print(num[i])
