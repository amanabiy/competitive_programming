class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
            [ 1, 2 , 3 , 2 , 1 ]
          3   0  0   1   1   1
          2   0  1   
          1
          4
        """
        dp = [[0 for _ in range(len(nums1) + 1)] for _ in range(len(nums2) + 1)]
        ans = 0 
        
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums2[i] == nums1[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    if ans < dp[i + 1][j + 1]:
                        ans = dp[i + 1][j + 1]

        return ans