
file = open('condingal.txt','r')
print(file.read())
file.close()

file = open('condingal.txt','r')
print("\n Read in parts\n")
print(file.read(8))
file.close()

file = open('condingal.txt','a')
file.write('hi! I am sinmayan.I am 13 years old.')
file.close()

