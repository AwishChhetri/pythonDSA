#Brute force approch
def check_bit(n, i):
    binary = bin(n)[2:]
    if len(binary) < i:
        return False
    print(binary)
    print(binary[-(i+1)], 1)
    return binary[-(i+1)] == '1'  

print(f"Status: ",check_bit(10,1))


#Optimal solution

def check_bit_O(n, i):
    print(f"Right shift: {1<<i}")
    if n & (1<<i) != 0:
        return True
    else:
        return False
print(f"Optimal Status:", check_bit_O(5,0))