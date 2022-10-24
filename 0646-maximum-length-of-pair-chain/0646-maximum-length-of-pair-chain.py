class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """
        """
        
        pairs.sort(key=lambda x: x[1])
        prev = float('-inf')
        ans = 0

        for a, b in pairs:
            if prev < a:
                ans += 1
                prev = b
        
        return ans