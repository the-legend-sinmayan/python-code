def romantoint (romaninput):
    roman={'M':1000,'D':500,'C':100,"l":50,"X":10,"v":5,'I':1}

    resultinteger = 0

    for i in range(0, len(romaninput)-1):
        if roman(romaninput[[i]])< roman[romaninput[i+1]]:
            resultinteger-= roman[romaninput[i+1]]
        else:
            resultinteger += roman[romaninput[i+1]]
        return resultinteger + roman[romaninput[-1]]
    
roman = input("input roman numeral:")

print("integer equvalent: ",romantoint(roman))