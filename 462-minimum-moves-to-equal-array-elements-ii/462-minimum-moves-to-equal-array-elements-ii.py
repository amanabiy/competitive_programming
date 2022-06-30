class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        middle = (nums[-1] + nums[0]) // 2
        middian = 0
        n = len(nums)
        if len(nums) % 2 == 0:
            middian = (nums[(n+1)//2] + nums[(n-1)//2])//2
        else:
            middian = nums[n//2]
        
        change = 0
        
        for i in nums:
            change += abs(i - middian)
            
        return change
        