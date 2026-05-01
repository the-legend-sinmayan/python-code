with open('condingal.txt') as fp:
    data1 = fp.read()

with open('my_file.txt') as fp:
    data2 = fp.read()


data1 +="\n"
data1 += data2
print("merging two files.............")
with open('merged_file.txt', 'w') as fp:
    fp.write(data1)
