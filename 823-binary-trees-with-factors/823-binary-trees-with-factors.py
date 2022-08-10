class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """
        2, 4
        2
        4, 2, 2
        2
        4 [4,2,2]
        5
               100
            10    10
           5 2   2  5
              20
            4   5
          2  2
          
         20
        2 10
          2 5     
        
        """
        memo = defaultdict(int)
        arr.sort()
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    memo[arr[i]] += (memo[arr[j]] * memo[arr[i] // arr[j]])
            memo[arr[i]] += 1

        return sum(memo.values()) % (10**9 + 7)