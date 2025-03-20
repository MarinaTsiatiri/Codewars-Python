def high(x):
    words = x.split()
    max_score = 0
    highest_word = ""
    
    for w in words:
        score = sum(ord(l) - ord('a') + 1 for l in w)
        if score > max_score:
            max_score = score
            highest_word = w
            
    return highest_word
