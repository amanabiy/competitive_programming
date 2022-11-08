class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        011
        101
        
        110
        """
        
        distinct = 0
        setBit = 0
        
        for num in nums:
            distinct ^= num
        
        # find the a set bit in the distinct
        for i in range(32):
            if distinct & (1 << i):
                setBit = i
                break
        
        one = 0
        # xor all the elements which have the setBit set
        for num in nums:
            if num & (1 << setBit):
                one ^= num
        
        return [one, distinct ^ one]