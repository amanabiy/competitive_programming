class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        self.considered = 0
        
        def backtrack(i):
            if i >= len(nums):
                self.considered += 1
                
            tried = set()
            for j in range(i, len(nums)):
                # check validity before swap
                if nums[i] == nums[j] and i != j or nums[j] in tried:
                    continue
                    
                nums[i], nums[j] = nums[j], nums[i]
                skip = False

                if i > 0:
                    x = sqrt(nums[i - 1] + nums[i])
                    if x != int(x):
                        skip = True
                if not skip:
                    backtrack(i + 1)

                nums[i], nums[j] = nums[j], nums[i]
                tried.add(nums[j])
        
        backtrack(0)
        return self.considered