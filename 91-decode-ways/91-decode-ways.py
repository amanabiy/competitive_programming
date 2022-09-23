class Solution:

    def numDecodings(self, s: str) -> int:
        letters = {}
        start = ord('A')
        memo = [float('inf')] * len(s)
        for i in range(start, ord('Z') + 1):
            letters[chr(i)] = i - start + 1
        
        def findWays(i):
            if i >= len(s):
                return 1
            if memo[i] != float('inf'):
                return memo[i]
            
            one, two = 0, 0
            
            if s[i] != '0':
                one = findWays(i+1)
                if i < len(s) - 1 and s[i:i+2] <= '26':
                    two = findWays(i+2)

            memo[i] = two + one
            return memo[i]
        
        return findWays(0)