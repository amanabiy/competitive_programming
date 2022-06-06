class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        """
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if str(nums[i]) + str(nums[j]) > str(nums[j]) + str(nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
        
        nums = list(map(str, nums))
        return str(int(''.join(nums)))
        