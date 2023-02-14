class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        countDigits = Counter(str(n))
        
        # generate all the 2 the power of nums
        for i in range(32):
            tempCount = Counter(str(1 << i))
            if tempCount == countDigits:
                return True
        
        return False