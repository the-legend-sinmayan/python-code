from math import sqrt



for k in range(2,int(sqrt(number))+1):
    if (input % k)==0:
        print(input, "is not a prime number")
        break
    else:
        print(input, "is a prime number")