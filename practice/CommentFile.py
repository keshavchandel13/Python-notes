def copy_script_without_comments(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            lines = src.readlines()
        
        with open(destination_file, 'w') as dest:
            for line in lines:
                if not line.strip().startswith('#'):
                    dest.write(line)
        
        print("Script copied successfully without comments.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the source and destination file paths
source_file = 'source_script.py'
destination_file = 'destination_script.py'

# Call the function to copy the script without comments
copy_script_without_comments(source_file, destination_file)
