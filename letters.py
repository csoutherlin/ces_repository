def letter_combinations(digits): #23

    if not digits:
        return []
    
    phone_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    def backtrack(index, path):

        if len(path) == len(digits):
            results.append("".join(path))
            return

        possible_letters = phone_map[digits[index]]

        for letter in possible_letters:
            # a
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    results = []
    backtrack(0, [])
    return results

print(letter_combinations("23"))