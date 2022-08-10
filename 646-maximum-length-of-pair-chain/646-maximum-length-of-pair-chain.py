class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        memo = [1 for i in range(len(pairs))]
        
        for i in range(len(pairs)):
            max_to_add = 0
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    max_to_add = max(max_to_add, memo[j])
            memo[i] += max_to_add
        
        return max(memo)