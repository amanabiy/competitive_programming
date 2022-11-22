class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        def dfs(i, previousWidth, prevMaxHeight, memo = {}):
            if i >= len(books):
                return prevMaxHeight

            state = (i, previousWidth)
            if state in memo:
                return memo[state]
            
            combine = float('inf')
            if previousWidth + books[i][0] <= shelfWidth:
                combine = dfs(i + 1, previousWidth + books[i][0], max(prevMaxHeight, books[i][1]))
            newRow = dfs(i + 1, books[i][0], books[i][1]) + prevMaxHeight
            
            memo[state] = min(combine, newRow)
            return memo[state]
        
        return dfs(0, 0, 0)
    
        """
        12 -> 3
        345  -> 3
        67 -> 2
        total -> 8
        
        I am not sure whether to combine it with or just combine it with the next one
        1 -> whether to take 1 or just combine it with the privious one
        
        """
                