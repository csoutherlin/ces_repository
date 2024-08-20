#from typing import List

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)
        complements = {3: 0, 4: 1}
        for i in range(length):
            if nums[i] in complements:
                return [i, complements[nums[i]]]
            else: 
                complement = target - nums[i]
                complements[complement] = i
        return []