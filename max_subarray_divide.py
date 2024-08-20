def max_crossing_sum(arr, l, m, h):
    sm = 0
    left_sum = float('-inf')
    right_sum = float('-inf')

    for i in range(m, l-1, -1):
        sm = sm + arr[i]
        if sm > left_sum:
            left_sum = sm
    sm = 0
    for i in range(m+1, h+1):
        sm = sm + arr[i]
        if sm > right_sum:
            right_sum = sm

    return left_sum + right_sum

def max_subarray_sum(arr, l, h):
    if l == h:
        return arr[l]
    
    m = (l + h) // 2

    return max(max_subarray_sum(arr, l, m), max_subarray_sum(arr, m+1, h), max_crossing_sum(arr, l, m, h))
    

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
max_sum = max_subarray_sum(arr, 0, n-1)
print("maximum contiguous sum is", max_sum)