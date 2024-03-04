def threeSum(nums):
    answer = []
    if len(nums) < 3:
        return answer

    nums.sort()  # Sort the array

    for i in range(len(nums) - 2):
        # Skip duplicate values for i
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                answer.append([nums[i], nums[left], nums[right]])
                # Skip duplicate values for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return answer

# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
result = threeSum(nums)
print(result)
