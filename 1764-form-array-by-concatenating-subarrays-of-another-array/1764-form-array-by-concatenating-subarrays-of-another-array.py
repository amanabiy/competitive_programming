class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        index = 0
        i = 0
        j = 0
        while i < len(nums):
            temp = i
            j = 0
            while i < len(nums) and j < len(groups[index]):
                if groups[index][j] == nums[i]:
                    i += 1
                    j += 1
                else:
                    i = temp + 1
                    break

            if j == len(groups[index]):
                index += 1

            if index == len(groups):
                break
            
        return index == len(groups) 