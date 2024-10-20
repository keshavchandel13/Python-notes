#Problem: 1
'''
s1=input("Enter the string 1: ")
s2=input("Enter the string 2: ")
print(id(s1[0]))  
print(id(s1[1]))
'''

#Problem:2
'''
s2[1]=s1[0] #throws error because string is immutable
'''

#Problem:3
'''
firstName=input("Enter your first your name ")
lastName=input("Enter your last your name ")
print(lastName+" "+firstName)
'''
#Problem:4
s_ref='''The piano sat silently in the corner of the room. Nobody could remember the last time it had
been played. The little girl walked up to it and hit a few of the keys. The sound of the piano rang
throughout the house for the first time in years. In the upstairs room, confined to her bed, the owner of
the house had tears in her eyes.'''

# to count the word 'piano'

cnt=s_ref.count("piano",0,len(s_ref))
print("The number of times 'Piano' repeated is: ",cnt);

#the index of 'piano'
ind=s_ref.index("piano")
print("The index at which piano is: ",ind);

# replace the word 'piano' to 'guitar'
print(s_ref.replace("piano","guitar"));