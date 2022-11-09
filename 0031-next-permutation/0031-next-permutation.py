class Solution:
    def bubbleSort(self, startIndex, endIndex, nums):
        for i in range(startIndex, endIndex):
            for j in range(startIndex, endIndex - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        the next permutation of the element is higher than my current
        [2, 3, 1] -> [3, 2, 1]
        [2, 3, 4] -> [2, 4, 3]
        [2, 1, 4, 3] -> [2, 3, 1, 4]
        
        [3, 2, 1] -> [1, 2, 3]
        [2, 2, 2] -> [2, 2, 2]
        [4,2,0,2,3,2,0]  -> [4, 2, 2, ]
        [4,2,0,3,2,2,0]
        
        """
        swaps = [float('-inf'), float('inf')] # [smallerIndex, largerIndex] -> tobe swapped
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                # try to swap the digits and then sort the left part
                if nums[j] < nums[i] and (swaps[0] < j or( swaps[0] == j and nums[swaps[1]] > nums[i])):
                    swaps = [j, i]

        if swaps[0] != float('-inf'): 
            nums[swaps[0]], nums[swaps[1]] = nums[swaps[1]], nums[swaps[0]]
            self.bubbleSort(swaps[0] + 1, len(nums), nums)
            return nums
        
        self.bubbleSort(0, len(nums), nums)
        return nums
        