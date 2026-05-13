def OnsquareTime(n):
    iterations=0
    for i in range(0,n):
        for j in range(0,n):
            print("*", end ="")
            iterations+=1
            print("")
            print("\nwhen n is ",n,"iterations=",iterations,"\n")


OnsquareTime(5)
OnsquareTime(4)
OnsquareTime(3)
print("\nwith evry'n' the time taken equals n2")
print("0(n2)")