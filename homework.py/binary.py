def binary_to_decimal(binary_str):
    # Convert binary string to decimal using int() with base 2
    decimal_value = int(binary_str, 2)
    return decimal_value

# Driver code
binary_input = input("Enter your Binary: ")
decimal_output = binary_to_decimal(binary_input)
print("Decimal :", decimal_output)
