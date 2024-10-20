""" A module is a file containing code written by somebody else which can be imported and used in our programs
 PIP--> it is a package installer for python,
eg--> pip install pyjokes (pyjoke is a module)
"""  

import pyjokes  #import  is used to import module in the program
joke=pyjokes.get_joke()
print(joke)