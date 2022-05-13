class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """
        1 0 1 0
        0 1 1 1
        
        0 0 0 1 1
        1 0 0 0 0 
        """
        count = 0
        num1 = list(reversed(bin(start)[2:]))
        num2 = list(reversed(bin(goal)[2:]))

        diff = abs(len(num1) - len(num2))
        
        num1 = num1 + ["0"] * diff
        num2 =  num2 + ["0"] * diff
        
        for i in range(min(len(num1), len(num2))):
            if int(num1[i]) ^ int(num2[i]):
                count += 1
        
        return count
