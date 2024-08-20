def max_subarray_sum(k, arr):
    max_sum = 0
    win_sum = 0
    win_start = 0

    for win_end in range(len(arr)):
        win_sum += arr[win_end]        

        if win_end >= k - 1:
             max_sum = max(max_sum, win_sum)
             win_sum -= arr[win_start]
             win_start += 1

    return max_sum

print(max_subarray_sum(4, [1, 4, 2, 10, 23, 3, 1, 0, 20])) # output: 39