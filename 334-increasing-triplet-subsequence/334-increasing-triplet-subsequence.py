class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        [1,2,3,4,5]
        [5,4,8,2,1,3,5,6]
        [1,(1,4),(2,8),,4,5,6]
        minms = [1,3]
        """
        mins = [float('inf'), float('inf')]
        
        for num in nums:
            if mins[0] >= num:
                mins[0] = num
            elif mins[1] >= num:
                mins[1] = num
            else:
                return True
        
        return False