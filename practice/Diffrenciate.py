'''Write a program to dierentiate between le_input.readline(n) and le_input.readlines()
statements..'''
# Create a sample text file
with open("sample.txt", "w") as file:
    file.write("Line 1: Hello World\n")
    file.write("Line 2: Python Programming\n")
    file.write("Line 3: File Handling\n")

# Open the file for reading
with open("sample.txt", "r") as file_input:
    # Using readline(n) to read the first n characters of the first line
    first_line_part = file_input.readline(10)
    print("Using readline(10):")
    print(first_line_part)

    # Reset the file pointer to the beginning of the file
    file_input.seek(0)

    # Using readlines() to read all lines into a list
    all_lines = file_input.readlines()
    print("\nUsing readlines():")
    print(all_lines)
