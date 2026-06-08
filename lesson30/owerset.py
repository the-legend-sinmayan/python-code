import math;
def printPowerSet(set, set_size):
    pow_set_size = (int)(math.pow(2, set_size));
    outer = 0;
    inner = 0;
     
    for outer in range(0, pow_set_size):
        for inner in range(0, set_size):
            if((outer & (1 << inner)) > 0):
                print(set[inner], end = "");
        print("")
size = int(input("Enter array size: "))


set = []
for i in range(0, size):
    n = int(input("Enter element: "))
    set.append(n)

printPowerSet(set, len(set))