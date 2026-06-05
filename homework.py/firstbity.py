import math

def rightmost_set_bit_position(n: int) -> int:
    if n == 0:
        return -1  # No set bit
    return int(math.log2(n & -n)) + 1

# Main program
num = int(input("Enter number: "))
pos = rightmost_set_bit_position(num)

# Show binary representation alongside result
print(f"Enter number: {num} ({bin(num)[2:]})")
if pos == -1:
    print("No set bit found.")
else:
    print(f"Position of the first set bit: {pos}")
