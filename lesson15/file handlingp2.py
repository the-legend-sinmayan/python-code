new_file = open('new_file.txt', 'x')
new_file.close()

import os
print("checkingif my_file exist or not...........")
if os.path.exists("my_file.txt"):
   os.remove("my_file.txt")
else:
    print("the file does not exist")


my_file = open('my_file.txt', 'w')
my_file.write("hi! i am sinmyan and i am 13 years old")
my_file.close()

os.remove('condingal.txt')

os.rmdir('folder')