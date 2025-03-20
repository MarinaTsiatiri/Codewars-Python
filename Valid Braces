def valid_braces(string):

    final = []
    braces = {')': '(', '}': '{', ']': '['}

    for char in string:
        if char in braces.values():
            final.append(char)
        elif char in braces:
            if final and final[-1] == braces[char]:
                final.pop()
            else:
                return False
    
    return len(final)==0
