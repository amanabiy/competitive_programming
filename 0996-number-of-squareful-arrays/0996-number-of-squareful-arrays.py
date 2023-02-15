class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        considered = set()
        
        def backtrack(i):
            if i >= len(nums):
                x = "".join(map(str, nums))
                if x in considered:
                    return
                considered.add(x)
                
                
            for j in range(i, len(nums)):
                # check validity before swap
                if nums[i] == nums[j] and i != j:
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
        
        backtrack(0)
        return len(considered)