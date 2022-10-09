class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        [2,2,2,1,2,2,1,2,1,2], k = 2
      [0,0,0,0,1,1,1,2,2,3,3]  ->  16 -> how do I know that
                                k -> 2
         0 - 4                k - 2 = y
                              2 - 2 = 0
                              2 - 2 = 0
                              3 - 2 = 1
                              3 - 2 = 1
        countOFOdd = 1
        ans = 4 + 4 + 3 + 3 = 14
        
        """
        hashtable = defaultdict(int)
        hashtable[0] = 1
        count = 0
        ans = 0
        
        for i in nums:
            if i % 2 == 1:
                count += 1
            if count >= k:
                ans += hashtable[count - k]
            hashtable[count] += 1
        
        return ans
        