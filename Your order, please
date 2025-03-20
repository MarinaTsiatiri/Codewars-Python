def order(sentence):
    words = sentence.split()
    sorted_words = [None] * len(words)
    
    for w in words:
        for l in w:
            if l.isdigit():
                sorted_words[int(l)-1] = w             
    
    return ' '.join(sorted_words) 
