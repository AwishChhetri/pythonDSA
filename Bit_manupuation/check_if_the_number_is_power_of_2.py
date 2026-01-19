def check_Power(n):
    return n > 0 and (n & (n-1)) == 0

print(f"Status:{check_Power(16)}")