'''Write a program that copies rst 10 bytes of a binary le into another binary l'''
def copy_first_10_bytes(source_file, destination_file):
    try:
        with open(source_file, 'rb') as src:
            # Read the first 10 bytes from the source file
            data = src.read(10)
        
        with open(destination_file, 'wb') as dest:
            # Write the first 10 bytes to the destination file
            dest.write(data)
        
        print("First 10 bytes copied successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the source and destination file paths
source_file = 'source.bin'
destination_file = 'destination.bin'

# Call the function to copy the first 10 bytes
copy_first_10_bytes(source_file, destination_file)
