num = int(input("input ur number: "))


digits  = len(str(num))

resultsNUmbers = 0

temp = num
while temp > 0 :
    digit = temp%  10
    resultsNUmbers+= digit **digits
    temp//= 10

if num == resultsNUmbers:
    print(num,"is an amstrong number")
else:
    print(num,"is not an amstrong number")