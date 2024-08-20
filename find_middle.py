def find_middle(arr):
    slow = 0
    fast = 0

    while fast < len(arr) - 1:
        fast += 2
        slow += 1
         
    return arr[slow]

# example usage

arr = [1, 2, 3, 4, 5]
print(find_middle(arr)) # output = 3

arr = [1, 2, 3, 4, 5, 6]
print(find_middle(arr)) # output = 4