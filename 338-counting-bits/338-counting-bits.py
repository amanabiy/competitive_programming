class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        0
        1
        
        """
        ans = [0]

        for i in range(1, n + 1):
            count = ans[i & (i - 1)] + 1
            ans.append(count)
        
        return ans