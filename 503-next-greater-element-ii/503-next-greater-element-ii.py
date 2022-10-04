class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        ans = [ -1 for i in range(len(nums))]
        stack = []
        
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        print(stack)
        curr = 0
        while stack and curr < len(nums):
            while nums[curr] > nums[stack[-1]]:
                ans[stack.pop()] = nums[curr]
            curr += 1
        
        return ans