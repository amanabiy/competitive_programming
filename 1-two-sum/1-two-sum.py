class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for i, num in enumerate(nums):
            if num in found:
                return [found[num], i]
            found[target - num] = i
