class Solution:
    def knightDialer(self, n: int) -> int:
        paths = {
            1: [8, 6],
            2: [7, 9],
            3: [8, 4],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [6, 2],
            8: [1, 3],
            9: [4, 2],
            0: [6, 4],
            -1: [1,2,3,4,5,6,7,8,9,0],
        }
        
        @lru_cache
        def dfs(prev, n):
            if n <= 0 or prev == 5:
                return n == 0

            ans = 0
            for neigh in paths[prev]:
                ans += dfs(neigh, n - 1)

            return ans % (10**9 + 7)
        
        return dfs(-1, n)
        