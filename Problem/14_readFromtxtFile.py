file_path = r"C:\Python\Problem\test3.txt"
with open(file_path, 'r') as data:
    poem = data.read()

if "twinkle" in poem.lower():
    print("word found")