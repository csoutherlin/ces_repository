def backspace_compare(s, t):
    
    def next_valid_char_index(string, index):
        skip = 0
        while index >= 0:
            if string[index] == '#':
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                return index    
            index -= index
        return -1
    
    i = len(s) - 1
    j = len(t) - 1

    while i >= 0 or j >= 0:
        i = next_valid_char_index(s, i)
        j = next_valid_char_index(t, j)

        if i >= 0 and j >= 0 and s[i] != s[j]:
            return False
        
        if (i >= 0) != (j >= 0):
            return False
        
        i -= 1
        j -= 1

    return True

print(backspace_compare("ab#c", "ad#c")) # true