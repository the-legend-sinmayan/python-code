
with open("Sample_File.txt", "r") as f:
    contents = f.read()
    print("Full contents of the file:\n", contents)

# 2. Print the first ten characters of the file
with open("Sample_File.txt", "r") as f:
    first_ten = f.read(10)
    print("First 10 characters:", first_ten)

# 3. Print the first line of the file
with open("Sample_File.txt", "r") as f:
    first_line = f.readline()
    print("First line:", first_line)

# 4. Print the first four lines of the file
with open("Sample_Fie.txt", "r") as f:
    for i in range(4):
        line = f.readline()
        print(f"Line {i+1}:", line.strip())


with open("Sample_File.txt", "r") as f:
    for line in f:
        print(line.strip())

f = open("Sample_File.txt", "r")
print(f.read())
f.close()
