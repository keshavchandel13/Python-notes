# Create SampleInput1.txt
with open('SampleInput1.txt', 'w', encoding="utf-8") as file1:
    file1.write("Name: ABC\n")
    file1.write("Batch:CS12\n")
    file1.write("Roll No.: 123\n")

# Create SampleInput2.txt
with open('SampleInput2.txt', 'w', encoding="utf-8") as file2:
    file2.write("City : PQR\n")
    file2.write("District: LMN\n")
    file2.write("State: XYZ\n")

# Combine contents into CombinedOutput.txt
with open('CombinedOutput.txt', 'w', encoding="utf-8") as outfile:
    # Read from SampleInput1.txt and write to CombinedOutput.txt
    with open('SampleInput1.txt', 'r', encoding="utf-8") as file1:
        for line in file1:
            outfile.write(line)
    
    # Read from SampleInput2.txt and write to CombinedOutput.txt
    with open('SampleInput2.txt', 'r', encoding="utf-8") as file2:
        for line in file2:
            outfile.write(line)

print("Files created and combined successfully!")
