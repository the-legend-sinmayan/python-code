def NunberOfBits(n):
    obes=0
    zero=0

    while(n):

        if(n&1==1):
            obes+=1
        else:
            zeros+=1

            n>>1

        print("\n\nones=",obes,"\nzeros",zero)

    number = int(input("Enter your number: "))

    NunberOfBits(number)