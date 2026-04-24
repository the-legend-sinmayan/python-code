file_read = open('Codingal.txt')
print("file in read mode")
print(file_read.read())
file_read.close()

file_write = open('Codingal.txt', 'w')
file_write.write("file in write mode.............")   
file_write.close()

file_append = open('Codingal.txt', 'a')

file_append.write("\nfile in append mode.............")
file_append.write("HI! I am sinmayan.I am 14 years old.")
file_append.close()