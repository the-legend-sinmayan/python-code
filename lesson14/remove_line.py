file1 = open('condingal.txt','r')
file2 = open('condingalupdated.txt','w')


for line in file1.readlines():
    if not line.startswith('coding'):
        print(line)
        file2.write(line)
file1.close()
file2.close()