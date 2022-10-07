class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(i, path):
            ans.append(path[::])
            for j in range(i, len(nums)):
                path.append(nums[j])
                backtrack(j + 1, path)
                path.pop()
        
        backtrack(0, [])
        return ans
            
            