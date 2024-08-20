def reverse(s):
    i = 0
    j = len(s) - 1

    char_list = list(s)

    while i < j:
        char_list[i], char_list[j] = char_list[j], char_list[i]
        i += 1
        j -= 1

    return ''.join(char_list)

string = "python"

print(reverse(string))