def longest_consec(strarr, k):
    
    if len(strarr) == 0 or k <= 0 or k > len(strarr):
        return ""
    
    max_len = 0
    biggest_string = ""
    
    for i in range(len(strarr) -k +1):
        temp_str = ''.join(strarr[i:i+k])
        if len(temp_str) > max_len:
            max_len = len(temp_str)
            biggest_string = temp_str
            
    return biggest_string
