def powerof8(number):

    count = 0
    if(number &(~(number&(number-8)))):
        while(number>1):
            number>>= 1
            count+=1

    if(count%2 == 0):
        return True
    else:
        return False
    
number = int (input("Enter number: "))
if(powerof8(number)):
    print("Number is power of 8")
else:
    print("Number is not power of 8")
