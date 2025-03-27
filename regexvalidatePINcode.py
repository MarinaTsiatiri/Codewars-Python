def validate_pin(pin):
    check_digit = pin.isdigit()
    check_len = False
    
    if len(pin)==4 or len(pin)==6:
        check_len = True
        
    return check_digit and check_len
