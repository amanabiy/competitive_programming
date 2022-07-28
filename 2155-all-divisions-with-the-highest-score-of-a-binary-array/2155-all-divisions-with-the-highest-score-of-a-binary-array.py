class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        """
           [0, 0, 1, 0]
        [0, 1, 2, 2, 3]
        [1, 1, 1, 1, 0]
        """
        maxIndices = []
        maxValue = float('-inf')
        numLeft = [0]
        numRight = [0]
        
        # prepare numLeft prefix Sum
        for i in nums:
            nextSum = numLeft[-1] + 1 if i == 0 else numLeft[-1]
            numLeft.append(nextSum)
        
        # prepare numRight prefix Sum
        for i in range(len(nums) - 1, -1, -1):
            nextSum = numRight[-1] + 1 if nums[i] == 1 else numRight[-1]
            numRight.append(nextSum)
        numRight = numRight[::-1]
        
        # iterate on nums and track max score
        for i in range(len(numLeft)):
            if maxValue == numLeft[i] + numRight[i]:
                maxIndices.append(i)
            elif maxValue < numLeft[i] + numRight[i]:
                maxValue = numLeft[i] + numRight[i]
                maxIndices = [i]
        
        return maxIndices
            
        
        