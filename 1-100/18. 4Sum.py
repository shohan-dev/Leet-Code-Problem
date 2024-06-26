from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def Nsum(nums: List[int], target: int, N: int, result: List[int], Nsums: List[List[int]]):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:
                return
            elif N == 2:
                j, k = 0, len(nums) - 1
                while j < k:
                    s = nums[k] + nums[j]
                    if s > target:
                        k -= 1
                    elif s < target:
                        j += 1
                    else:
                        Nsums.append(result + [nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while nums[j-1] == nums[j] and j < k:
                            j += 1
                        while nums[k+1] == nums[k] and k > j:
                            k -= 1
            else:
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        Nsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], Nsums)
        
        nums.sort()
        foursums=[]
        Nsum(nums,target,4,[],foursums)
        return foursums
