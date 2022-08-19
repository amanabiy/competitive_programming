class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        ans = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            # print(nums[mid], left, right, mid)
            if mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                if (right - mid + 1) % 2:
                    left = mid
                else:
                    right = mid - 1
            elif mid > 0 and nums[mid] == nums[mid - 1]:
                if (mid - left + 1) % 2:
                    right = mid
                else:
                    left = mid + 1
            else:
                return nums[mid]
    
        return mid