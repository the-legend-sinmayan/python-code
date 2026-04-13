my_set = {1,2,2,3,4,4,4}
print("set :", my_set)

my_set.add(5)
print("updated set:",my_set)

set1 = my_set
set2 = {4,5,6,7,8}

print ("\nset1:", set1)
print ("set2:", set2)
print("difference")
print(set1.difference(set2))
print("symmetric difference")
print(set1.symmetric_difference(set2))