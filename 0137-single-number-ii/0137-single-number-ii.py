class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        
        for num in nums:
            # add it to twos if it was already added on ones            
            twos |= (ones & num)
            
            # add it to ones if it wasn't there or remove it if it was there
            ones ^= num
            
            # if it is in both ones and twos remove it from both
            in_both = (twos & ones)
            ones &= ~(in_both)
            twos &= ~(in_both)
        
        return ones