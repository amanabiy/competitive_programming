class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = float('inf')
        
        for i in range(0, len(blocks) - k + 1):
            ans = min(ans, blocks[i:i+k].count('W'))
        
        return ans