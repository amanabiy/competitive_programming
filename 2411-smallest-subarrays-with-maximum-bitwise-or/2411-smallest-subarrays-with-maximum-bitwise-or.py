class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        """
        """
        latest = [0] * 32
        ans = []
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range(32):
                if nums[i] & (1 << j):
                    latest[j] = i
            ans.append(max(1, max(latest) - i + 1))
        
        return ans[::-1]
        
        
        
        