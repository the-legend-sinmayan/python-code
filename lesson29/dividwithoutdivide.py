def divide(ourdividend, ourdivisor):
    sign =(-1 if((ourdividend<0) ^ (ourdivisor<0)) else 1)
    ourdividend = abs(ourdividend)
    ourdivisor = abs(ourdivisor)

    quotient = 0
    tempnum = 0

    for i in range(31, -1, -1):
        if tempnum + (ourdivisor << i) <= ourdividend:
            tempnum += ourdivisor << i
            quotient |= 1 << i
    if sign==-1:
        quotient = -quotient
    return quotient

a=int(input("Enter a for a/b: "))
b=int(input("Enter b for a/b: "))
print("results of",a,"/",b,"is",divide(a,b))
