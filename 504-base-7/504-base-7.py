class Solution:
    def convertToBase7(self, num: int) -> str:
        """
        0 1 2 3 4 5 6
        4
        4 % 2 -> 0
        2 % 2 -> 0
        1 % 2 -> 1
        """
        ans = []
        negative = True if num < 0 else False
        
        if num < 0:
            num *= -1
        
        while num:
            ans.append(f"{num % 7}")
            num //= 7
        
        if negative:
            ans.append("-")
            
        return "".join(reversed(ans)) or "0"