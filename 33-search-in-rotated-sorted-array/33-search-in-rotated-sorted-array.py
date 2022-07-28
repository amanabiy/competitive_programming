class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        [1,2,3,4,5,6,7,8]
        [4,5,6,7,8,1,2,3]
        """
        
        left = 0
        right = len(nums) - 1
        ans = -1

        
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            
            if nums[left] <= target:
                
                if nums[mid] > target or nums[mid] < nums[left]:
                    # print("here", left,nums[mid] > target, nums[mid] <= nums[left])
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:
                
                if nums[mid] < target or nums[mid] >= nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
                
            # print(left, right)
        
        return ans
        
        
