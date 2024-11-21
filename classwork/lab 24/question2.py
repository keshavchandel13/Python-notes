import os
print(f"The current working directory is: {os.getcwd()}")
current_dir = os.getcwd()
os.chdir('..')
os.mkdir('Outer_Directory')
print(f"The current working directory is: {os.getcwd()}")

os.chdir(current_dir)

os.mkdir('Inner_Directory')

 