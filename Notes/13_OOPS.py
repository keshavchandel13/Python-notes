class employee:
    lang="Python" #This is class attribute
    salary=1200000 #these atrributes directly belong to the class
keshav=employee()
keshav.name="Keshav chandel" #This is object attribute also known as instance attribute
print(keshav.name, keshav.lang, keshav.salary)

shivam=employee()
shivam.name="Shivam" #Instance attribute is given more priority
print(shivam.name, shivam.lang, shivam.salary)