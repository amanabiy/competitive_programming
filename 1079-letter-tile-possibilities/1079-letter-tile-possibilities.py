class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
        
        
        def backtrack():
            ans = 0
            for k in count:
                if count[k]:
                    count[k] -= 1
                    ans += backtrack() + 1
                    count[k] += 1
            
            return ans

        return backtrack()
        