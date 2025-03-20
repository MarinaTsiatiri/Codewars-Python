def dig_pow(n, p):
    digits = [int(digit) for digit in str(n)]
    total = sum(digit ** (p+i) for i,digit in enumerate(digits))
        
    if total%n==0:
        k = total/n
        return k
    return -1
        
