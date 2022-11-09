class Solution:
    def reverse(self, startIndex, endIndex, nums):
        endIndex -= 1
        while startIndex < endIndex:
            nums[startIndex], nums[endIndex] = nums[endIndex], nums[startIndex]
            startIndex += 1
            endIndex -= 1

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
        [4,2,0,3,2,2,0] -> [4,2,0,3,0,2,2]
             l
                   r
        """
        swap = float('inf') 
        currIndex = len(nums) - 1

        # continue searching where it gets lower
        while currIndex > 0:
            if nums[currIndex] > nums[currIndex - 1]:
                # find the position where this element belongs
                possiblePos = currIndex
                while possiblePos < len(nums) and nums[possiblePos] > nums[currIndex - 1]:
                    possiblePos += 1
                swap = possiblePos - 1
                break
            currIndex -= 1

        if swap != float('inf'):
            nums[swap], nums[currIndex - 1] = nums[currIndex - 1], nums[swap]
            self.reverse(currIndex, len(nums), nums)
            return nums
        
        self.reverse(0, len(nums), nums)
        return nums
        