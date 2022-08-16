class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        difference = {0: -1}
        prefixSum = 0
        max_ans = 0
        
        for i in range(len(nums)):
            prefixSum += nums[i] if nums[i] else -1
            if prefixSum in difference:
                max_ans = max(max_ans, i - difference[prefixSum])
            else:
                difference[prefixSum] = i
        
        return max_ans