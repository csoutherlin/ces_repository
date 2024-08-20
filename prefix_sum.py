def compute_prefix_sum(arr):

    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    return prefix_sum

arr = [3, 1, 4, 1, 5, 9, 2]
prefix_sum = compute_prefix_sum(arr)
print(prefix_sum)

left = 3
right = 6

def range_sum_query(prefix_sum, left, right):
    return prefix_sum[right + 1] - prefix_sum[left]