class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """
        -2
        [10 12 7 8 5 3 4 2 1]
         12 14 
        [1 1 1 1 2 3 3 1 1]
                     0 0 0
        """
        memo = defaultdict(int)
        for i in range(len(arr)):
            if arr[i] - difference in memo:
                memo[arr[i]] = max(memo[arr[i] - difference] + 1, memo[arr[i]])
            else:
                memo[arr[i]] = 1

        return max(memo.values())