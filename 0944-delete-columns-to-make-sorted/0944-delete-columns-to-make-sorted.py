class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        cols = len(strs[0])
        rows = len(strs)
        
        for col in range(cols):
            delete = False
            for row in range(rows - 1):
                if strs[row][col] > strs[row + 1][col]:
                    delete = True
                    break
            count += delete
        
        return count