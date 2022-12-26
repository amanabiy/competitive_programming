class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        nums = [2,2,3,4]
        
        
        """
        ans = 0
        nums.sort()
        n = len(nums)

        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1
            while left < right:
                # if possible to make triangle
                if nums[left] + nums[right] > nums[i]:
                    ans += right - left
                    right -= 1
                # if not increase your left
                else:
                    left += 1
        
        return ans
                
                