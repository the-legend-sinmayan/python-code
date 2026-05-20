numlargest = int(input("enter larggest number: "))
numbersmallest = int(input("enter smallest number: "))


while(numbersmallest):
    numberstore = numbersmallest
    numbersmallest = numlargest % numbersmallest
    numlargest = numberstore

print("HCF is:",numlargest)