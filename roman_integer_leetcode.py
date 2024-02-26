def romanToInt(s: str) -> int:
    # create a hash table to map each roman numeral to its corresponding value
    roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # initialize the result variable to zero
    result = 0
    #iterate over the input string from left to right
    for i in range(len(s)):
        # if the current character is smaller than the next character, subtract its value
        if i < len(s) -1 and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
            result -= roman_to_int[s[i]]
            # otherwise add its value to the result
        else:
            result += roman_to_int[s[i]]
        # return the result
        return result
    