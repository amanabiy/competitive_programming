class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        missed = 0

        for i in range(len(nums)):
            missed ^= i + 1
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
                missed ^= abs(nums[i])
            else:
                ans.append(abs(nums[i]))
            
        ans.append(missed)
        
        return ans