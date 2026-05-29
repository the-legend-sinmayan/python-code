def FirstSetBit(n):

    count =1


    while(n):


        if(n&1==1):
            break
        count+= 1

        n>>=1


        return count