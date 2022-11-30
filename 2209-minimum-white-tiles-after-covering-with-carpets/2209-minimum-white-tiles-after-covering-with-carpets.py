class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        """
        I need to find where the most of the white tiles lie
        10110101   len = 2 num = 2
        11233445
        
        3:
        2: 1
        1: 3
        
        
        """
        prefixSum = [0]
        for n in floor:
            prefixSum.append(prefixSum[-1] + int(n))
    
        def dfs(i, num, memo = {}):
            if i >= len(floor):
                if i >= len(floor):
                    i = len(floor)
                return prefixSum[-1] - prefixSum[i]

            state = (i, num)
            if state in memo:
                return memo[state]
            startHere = 1000
            if num > 0:
                startHere = dfs(i + carpetLen, num - 1, memo)
            skipIt = dfs(i + 1, num, memo) + int(floor[i])

            memo[state] = min(startHere, skipIt)
            return min(startHere, skipIt)
        
        
        return dfs(0, numCarpets)