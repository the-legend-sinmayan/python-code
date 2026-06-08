def reverse_bits(num):
    
    binary = bin(num)[2:]
    
   
    reversed_binary = binary[::-1]
   
    reversed_num = int(reversed_binary, 2)
    
    print(f"Original Number: {num} ({binary})")
    print(f"Reversed Number: {reversed_num} ({reversed_binary})")
    return reversed_num

reverse_bits(12)  
reverse_bits(11)  
