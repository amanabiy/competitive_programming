class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        pair = {}
        for index, val in enumerate(nums):
            pair[val] = index
        
        for from_v, to_v in operations:
            index = pair[from_v]
            nums[index] = to_v
            del pair[from_v]
            pair[to_v] = index
        
        return nums