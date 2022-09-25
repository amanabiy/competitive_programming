class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        0
        1
        
        """
        ans = []

        for i in range(n + 1):
            count = 0
            for j in range(32):
                if i & (1 << j):
                    count += 1
            ans.append(count)
        
        return ans