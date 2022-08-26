class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        2^0 - 1
        2^1 - 2
        2^2 - 4
        128
        |
        128
         |
        128
        
        
        """
        count = Counter(str(n))
        for i in range(31):
            if Counter(str(1 << i)) == count:
                return True
        return False