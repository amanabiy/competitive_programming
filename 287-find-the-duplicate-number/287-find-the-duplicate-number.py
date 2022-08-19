class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        numbers
        """
        def countFrequecy(nums, num):
            count = 0
            for i in nums:
                if i <= num:
                    count += 1
                
            return count
        
        
        left = 1
        right = len(nums) - 1
        ans = -1

        
        while left <= right:
            mid = left + (right - left) // 2
            count = countFrequecy(nums, mid)
            if count != 0 and count > mid:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
        