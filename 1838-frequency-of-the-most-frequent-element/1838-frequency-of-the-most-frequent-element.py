class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        [1,2,4] k = 5
        
        """
        nums.sort()
        ans = 1
        left = right = 0
        prefixSum = [0]
        
        for i in nums:
            prefixSum.append(prefixSum[-1] + i)
            
        while right < len(nums):
            
            # shift to the right and minus from your k sum(nums[left:right] + [0])
            useK = (nums[right] * (right - left)) - (prefixSum[right] - prefixSum[left])
            if  useK <= k and useK > -1:
                right += 1
            else:
                left += 1

            ans = max(ans, right - left)
            
        return ans
        