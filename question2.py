#function, that returns the first non-repeated character in the given string.
def first_non_repeated(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    for char in s:
        if char_count[char] == 1: 
            return char
    return None

