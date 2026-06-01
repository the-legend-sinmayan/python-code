def PrintTwoOdd(arr, size):
    xoro2 = arr[0]

    x = 0
    y = 0

    # XOR of all elements
    for i in range(1, size):
        xoro2 = xoro2 ^ arr[i]

    setbit = xoro2 & ~(xoro2 - 1)

    
    for i in range(size):
        if arr[i] & setbit:
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]

    print("The two odd elements are:", x, "and", y)


# Input array
arr = []
arr_size = int(input("Enter size of the array: "))

for i in range(arr_size):
    num = int(input("Enter number: "))
    arr.append(num)

PrintTwoOdd(arr, arr_size)