class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]

        for val in range(1, len(nums)):
            ans.append(ans[-1] + nums[val])
        
        return ans