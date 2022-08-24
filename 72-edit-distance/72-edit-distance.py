class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1, word2 = list(word1), list(word2)
        memo = {}

        def distance(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if not word1[i:] or not word2[j:]:
                return max(len(word1[i:]), len(word2[j:]))
            
            
            no_opration = inf
            if word1[i] == word2[j]:
                no_opration = distance(i + 1, j + 1)
            
            inserted = distance(i, j + 1) + 1
            deleted = distance(i + 1, j) + 1
            replace = distance(i + 1, j + 1) + 1
            
            memo[(i, j)] = min(inserted, deleted, replace, no_opration)
            return memo[(i, j)]
        
        return distance(0, 0)