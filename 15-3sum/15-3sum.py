class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        [-1,0,1,2,-1,-4]
        [-4,-1,-1,0,1,2] target = 0
        seen {
            -4, -1, 0, 
        }
        -4 -> 4
        -1
        -1 + -1 -> 2
        -1 + 0 -> 0 - -1 -> 1
        -1 + 1 -> 0 -> 0 + 0
        
        []
        [-1, 0, 1]
        """
        ans = set()
        n = len(nums)
        nums.sort()

        for i in range(n):
            seen = set()
            for j in range(i + 1, n):
                diff =  0 - (nums[i] + nums[j])
                if diff in seen:
                    ans.add((nums[i], diff, nums[j]))
                seen.add(nums[j])        
        
        return ans        