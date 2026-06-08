def totalFlips(num1,num2):
    flips = 0
    for i in range(32):
        t1= (num1 >> i) & 1
        t2= (num2 >> i) & 1
        if (t1 != t2):
            flips += 1
        num1>>=1
        num2>>=1
    return flips

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("\n NUmber of flips needed: ", totalFlips(num1, num2))
