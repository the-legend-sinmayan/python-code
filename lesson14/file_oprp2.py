file_read = open('condingal.txt','r')
print("file in read mode")
print(file_read.read())
file_read.close()

file_write = open('condingal.txt', 'w')

file_write.write("file in write mode.............")
file_write.write("HI! I am sinmayan.I am 13 years old.")
file_write.close()

file_append = open('condingal.txt', 'a')

file_append.write("\nfile in append mode.............")
file_append.write("HI! I am sinmayan.I am 13 years old.")
file_append.close()