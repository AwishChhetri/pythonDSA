# Count the number of set bits

# 1. Brute for approach
def count_set(n):
    binary = bin(n)[2:]
    count = 0
    for i in binary:
        if i == '1':
            count += 1
    return count

print(f"Bit set count: ", count_set(15))

# 2.Optimal approach

def count_set_O(n):
    count = 0
    while n!=0:
        n = n & (n -1)
        count += 1
    return count
print(f"Counter:{count_set_O(15)}")