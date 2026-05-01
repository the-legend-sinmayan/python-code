with open('condingal.txt', 'w') as file:
   file.write('HI! I am sinmyan and I am 13 years old')
   file.close()

with open('condingal.txt', 'r') as file:
   data =file.readlines()
   print("word in this dile are.............")
   for line in data:
      word = line.split()
      print(word)
      file.close()
