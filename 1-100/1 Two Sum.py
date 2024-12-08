from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            s = target - num
            if s in seen:
                return [seen[s], i]
            seen[num] = i