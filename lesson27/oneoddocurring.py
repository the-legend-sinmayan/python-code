def OddOcurring(arr):
    result = 0
    for i in arr:
        result = result ^ i
    return result

arr = []

n = int(input("Enter array size: "))

while n:
    num = int(input("Enter number: "))
    arr.append(num)
    n -= 1

print("\nOdd occurring number is:", OddOcurring(arr))