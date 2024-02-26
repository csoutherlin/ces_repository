def is_palindrome(x):
    # convert x to a string
    s = str(x)
    # reverse s
    r = s[::-1]
    # compare s and r
    return s == r

