import re

# Input text
# text = 'From: chandelkeshav4@gmail.com at 9:30 am'
with open('juit.txt', 'r') as f1:
    for line in f1:
        # Extract email and split it into username and domain
        match = re.search(r'(\S+)@(\S+)', line)  # One regex to capture both username and domain
        if match:
            username = match.group(1)  # Extract the part before @
            domain = match.group(2)  # Extract the part after @

            print("Username:", username)
            print("Domain:", domain)
            
            # Write username and domain to files
            with open('username.txt', 'a') as file:
                file.write(username+'\n')
            
            with open('domain.txt', 'a') as file:
                file.write(domain+'\n')
