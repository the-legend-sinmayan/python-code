my_tuple = ()
print(my_tuple)

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

my_tuple = (1, "hello",2,"sup",3.4)
print(my_tuple)

my_tuple = ("mouse", [8, 4, 6], (1, 2, 3), "keyboard")
print(my_tuple)

my_tuple =('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
print(my_tuple[0])
print(my_tuple[25])

n_tuple = ("mouse", [8, 4, 6], (1, 2, 3), "keyboard")

print(n_tuple[0][3])
print(n_tuple[1][1])

print("sliced:", my_tuple[0:3])

for letter in my_tuple:
    print("hello", letter)