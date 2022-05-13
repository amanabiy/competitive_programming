class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """
        1 0 1 0
        0 1 1 1
        
        0 0 0 1 1
        1 0 0 0 0 
        """
        count = 0
        num = bin(start ^ goal)
        return num.count("1")
