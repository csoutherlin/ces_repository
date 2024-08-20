def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

nums = [3, 2, 2, 3]
val = 3
k = remove_element(nums, val)
print("The number of elements not equal to val is:", k)
print("The modified array is:", nums[:k])