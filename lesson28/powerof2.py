def power2(number):
    if(number == 0):
        return 0
    if((number & (number - 1)) == number):
        return 1
    return 0

number = int (input("Enter number: "))

if(power2(number)):
    print("Number is power of 2")
else:
    print("Number is not power of 2")