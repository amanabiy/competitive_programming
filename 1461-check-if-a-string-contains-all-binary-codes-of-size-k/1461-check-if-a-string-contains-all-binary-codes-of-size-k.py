class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        """
        
        visited = set()
        
        for i in range(k, len(s)+1):
            num = 0
            count = k - 1
            for j in range(i-k, i):
                if s[j] == "1":
                    num += (2 ** count)
                count -= 1
            visited.add(num)
            
        return len(visited) == 2**k