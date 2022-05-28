class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)):
            missing = i ^ nums[i]
            if missing:
                return i

        return len(nums)