def find_equilibrium_sum(arr):
    n = len(arr)
    if n == 0:
        return -1
    
    def compute_prefix_sum(arr):
        n = len(arr)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
        return prefix_sum

    def compute_suffix_sum(arr):
        sux_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            sux_sum[i] = sux_sum[i + 1] + arr[i]
        return sux_sum
    
    suffix = compute_suffix_sum(arr)
    prefix = compute_prefix_sum(arr)

    for i in range(1, n - 1):
        if prefix[i] == suffix[i + 1]:
            return i
    return -1

arr = [-7, 1, 5, 2, -4, 3]
print("equilibrium index is:", find_equilibrium_sum(arr))
    
   