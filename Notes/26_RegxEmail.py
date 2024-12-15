import re

# Input text
text = 'From: chandelkeshav4@gmail.com at 9:30 am'

# Extract email and split it into username and domain
match = re.search(r'(\S+)@(\S+)', text)  # One regex to capture both username and domain
if match:
    username = match.group(1)  # Extract the part before @
    domain = match.group(2)  # Extract the part after @

    print("Username:", username)
    print("Domain:", domain)
    
    # Write username and domain to files
    with open('username.txt', 'w') as file:
        file.write(username)
    
    with open('domain.txt', 'w') as file:
        file.write(domain)
