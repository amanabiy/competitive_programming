class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binarySearch(arr, target):
            left = 0
            right = len(arr) - 1
            ans = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] == target:
                    ans = mid
                    break
                if arr[mid] < target:
                    left = mid + 1
                else:
                    ans = mid
                    right = mid - 1

            return ans
        
        collect = []
        
        for i in range(len(nums)):
            if not collect or nums[i] > collect[-1]:
                collect.append(nums[i])
            else:
                index = binarySearch(collect, nums[i])
                collect[index] = nums[i]
        
        return len(collect)