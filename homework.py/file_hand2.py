import os

with open("filename.txt", "w") as f:
    f.write("Hello, my name is Sinmayan. I enjoy gaming and coding.")

#
with open("filename.txt", "r") as f:
    contents = f.read()
    words = contents.split()
    print("Words in the file:", words)

# 3. Check whether a file named My_File exists or not
if os.path.exists("My_File.txt"):
    print("My_File.txt exists.")
else:
    print("My_File.txt does not exist.")

if not os.path.exists("My_File.txt"):
    with open("My_File.txt", "w") as f:
        f.write("Hello, my name is Sinmayan. I enjoy gaming and coding.")
    print("My_File.txt created and introduction written.")

# 5. Delete the file named sample_doc
if os.path.exists("Sample_File.txt"):
    os.remove("Sample_File.txt")
    print("Sample_File.txt deleted.")
else:
    print("Sample_File.txt not found.")

f = open("filename.txt", "r")
print(f.read())
f.close()

