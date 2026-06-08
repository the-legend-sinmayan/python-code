def longest_consecutive_ones(num):

    binary = bin(num)[2:]
    
    longest = max(len(block) for block in binary.split('0'))
    
    print(f"Original Number: {num} ({binary})")
    print(f"Longest consecutive 1’s length : {longest}")
    return longest


longest_consecutive_ones(56)  # Output: 3
