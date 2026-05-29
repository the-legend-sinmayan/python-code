def SetOrNot(number,n):
    if number & (1<<(n - 1)):
        print("\n set")
    else:
        print("\nnot set")

number  = int(input("enter ur number:  "))
n = int(input("enter bit number: "))
SetOrNot(number,n)