class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        missed = 0
        nums.sort()
        for i in range(len(nums) - 1):
            missed ^= i + 1
            if nums[i] == nums[i + 1]:
                ans.append(nums[i])
                continue
            missed ^= nums[i]

        missed ^= len(nums) ^ nums[-1]
        
        ans.append(missed)
        
        return ans