class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
            [ 1, 2 , 3 , 2 , 1 ]
          3   0  0   1   1   1
          2   0  1   
          1
          4
        """
        dp = [[0 for _ in nums1] for _ in nums2]
        ans = 0  
        
        # the first row to 1 if matched
        for i in range(len(nums1)):
            if nums1[i] == nums2[0]:
                dp[0][i] = 1
                ans = 1
            # if i > 0:
            #     dp[0][i] = max(dp[0][i], dp[0][i - 1])
        
        # the first col to 1 if matched
        for i in range(len(nums2)):
            if nums2[i] == nums1[0]:
                dp[i][0] = 1
                ans = 1

        
        for i in range(1, len(nums2)):
            for j in range(1, len(nums1)):
                if nums2[i] == nums1[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                if ans < dp[i][j]:
                    ans = dp[i][j]

        return ans