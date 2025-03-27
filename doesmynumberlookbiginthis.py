def narcissistic(value):
    power = len(str(value))
    digits = list(map(int, str(value)))
    total = 0
    
    for d in digits:
        total += pow(d,power)
    
    if total==value:
        return True
    return False
